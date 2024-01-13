print('Проверочный принт')

import requests
import json
import sys
import sqlite3
import pprint
from SCRIP_For_Clean_Tags import search_TAGS



STR = ['ВижнЛабс (VisionLabs)', 'SberTech', 'Компания 05.ру', 'Банк Открытие', 'ХОУМ Банк', 'СберМедИИ', 'Кухня на районе', 'ВкусВилл', 'СберМаркет', 'СБЕР', 'Альфа-Банк', 'РОСБАНК',
       'Почта Банк', 'ПСБ (ПАО «Промсвязьбанк»)', 'Банк ДОМ.РФ', 'Газпромбанк', 'РНКБ Банк (ПАО)', 'РНКБ Банк (ПАО)', 'Банк ВТБ (ПАО)', 'Тинькофф', 'СберСпасибо', 'МСП Банк',
       'БАНК УРАЛСИБ', 'Московская Биржа', 'Райффайзен Банк', 'Вкусно — и точка', 'SberAutoTech', 'Московский Кредитный Банк', 'Центральный банк Российской Федерации',
       'Finstar Financial Group', 'Ренессанс cтрахование, Группа', 'ФинГрад', 'Ингосстрах Банк', 'Красное & Белое, розничная сеть', 'Россельхозбанк', 'ОТП Банк, АО (OTP bank)',
       'СберЗдоровье', 'CarMoney', 'МТС Финтех', 'Бэнкс Софт Системс']
INTEREST_vac_num = ['ВижнЛабс (VisionLabs)_89997213', 'ФГБУ Авиаметтелеком Росгидромета', 'BI.ZONE', 'NGENIX', '', ]

def checkModeAndAmoLaunch():
    with open('app_elems.json', 'r', encoding='utf-8') as in_json:
        mode = json.load(in_json)
    return mode.get('mode'), mode.get('amoLaunches')


def zeroCurNumTgShipTime():
    '''
    Resetting the number of job postings to Telegram completed since the last session at a time
    '''
    with open('app_elems.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    data["numCurSend"] = 0

    with open('app_elems.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def bigReqToApiHh(page=0):
    params = {
        'text': 'Python программист',
        'experience': 'between1And3', 
        'area': 1,
        'per_page': 100,  # количество результатов на страницу (максимум 100)
        'page': page
    } # 'noExperience'
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    return response


def slidingOnVacancies(resFromApi):
    c = 0
    for i in resFromApi.json()['items']:
        c += 1
        print(i['employer']['name'])

##        if i['id'] == '91379400':
##            pp = pprint.PrettyPrinter(width=40, compact=True)
##            pp.pprint(i) #(resFromApi.json()['items'])
##            print(i)
        checkVacNum = isVacNumAlreadyInDB(i['id'])
##        print(i['id'], type(i['id']))
##    print(resFromApi.json())
    print(c)

def isVacNumAlreadyInDB(vacId):
    connection = sqlite3.connect('DBbigForNumsAndOthers.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT COUNT(*) FROM numsVerVacas WHERE numVacs = ?''', (vacId,))
    count = cursor.fetchone()[0]
    if count == 0:
        cursor.execute('''INSERT INTO numsVerVacas (numVacs) VALUES (?)''', (vacId,))
        print(F"elem {vacId} added")
    connection.commit()
    connection.close()

if __name__ == '__main__':
    check_mode = checkModeAndAmoLaunch()
    print(type(check_mode[1]))
    # There can be two modes: 1 - you can poll the api; 2 - a temporary pause
    if check_mode[0] == 1:
        zeroCurNumTgShipTime()
        responseToApi = bigReqToApiHh()
        print(responseToApi.json()['page'], len(responseToApi.json()['items']))
        slidingOnVacancies(responseToApi)
##        print(responseToApi.json()['pages'], type(responseToApi.json()['pages']))


        for page in range(1, responseToApi.json()['pages']):
            responseToApi = bigReqToApiHh(page)
            slidingOnVacancies(responseToApi)
##            print(page, responseToApi.json()['page'], len(responseToApi.json()['items']))


##        while responseToApi.json()['items']:
##            c = 0
##            for vac in responseToApi.json()['items']:
##                print(vac['id'])
##                c += 1
            
##        print(responseToApi.json())


##    params = {
##    'text': 'Python программист',
##    'experience': 'between1And3', 
##    'area': 1,
##    'per_page': 100,  # количество результатов на страницу (максимум 100)
##    'page': 8
##    } # 'noExperience'
##
##    print('Это params вначале:', params)
##    response = requests.get('https://api.hh.ru/vacancies', params=params)
##    print('This items: ',response.json()['items'])
##    for i in response.json():
##        print(i)
