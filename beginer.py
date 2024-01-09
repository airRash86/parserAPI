import requests
import json
import sys
from SCRIP_For_Clean_Tags import search_TAGS

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
##    print(sys.getsizeof(response.json()))
##    for i in response.json():
##        print(i)
##    print('Номер стр при первом запросе: ',response.json()['page'])
##    print('Номер стр при первом запросе: ',response.json()['pages'])



if __name__ == '__main__':
    check_mode = checkModeAndAmoLaunch()
    print(type(check_mode[1]))
    # There can be two modes: 1 - you can poll the api; 2 - a temporary pause
    if check_mode[0] == 1:
        zeroCurNumTgShipTime()
        responseToApi = bigReqToApiHh()
        print(responseToApi.json()['page'], len(responseToApi.json()['items']))
##        print(responseToApi.json()['pages'], type(responseToApi.json()['pages']))
        for page in range(1, responseToApi.json()['pages']):
            responseToApi = bigReqToApiHh(page)
            print(page, responseToApi.json()['page'], len(responseToApi.json()['items']))
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
