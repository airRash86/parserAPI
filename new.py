print('For chacking')

import requests
from SCRIP_For_Clean_Tags import search_TAGS

params = {
    'text': 'Python программист',
    'experience': 'between1And3', 
    'area': 1,
    'per_page': 100  # количество результатов на страницу (максимум 100)
} # 'noExperience'
response = requests.get('https://api.hh.ru/vacancies', params=params)

##for i in response.json():
##    print(i)
print('Номер стр при первом запросе: ',response.json()['page'])

#Тут храняться id вакансий банков:
banksSTORE = ['89841853', '86261194', '85105920', '89854893', '89854356']
randomSTORE = ['89312738', '90480744', '88925330', '90285918', '89544787']

while response.json()['items']:
    # обрабатываем результаты
    print('ok')
    c=0
    for item in response.json()['items']:
        
        # обрабатываем каждую вакансию, например, выводим заголовок
##        print(item['id'])

##        if item['id'] == '89400788':
##            print()
##            print(item['snippet']['requirement'])
##            print()

        if item['id'] in banksSTORE or item['id'] in randomSTORE:
            
##            pass
##            print()
##            print(item) #['snippet']['requirement'])
##            print(item["employer"]["name"])
##            print()

            response_1 = requests.get(F"https://api.hh.ru/vacancies/{item['id']}")
            full_vacancy_data = response_1.json()
            search_TAGS(full_vacancy_data["description"])
                            
            
        c +=1
    print('На стр вакансий: ', c)
    # Увеличиваем значение "страницы" для запроса следующей страницы результатов


    params['page'] = response.json()['page'] + 1
    response = requests.get('https://api.hh.ru/vacancies', params=params)
    print('Номер стр при каком-то послед запросе: ',response.json()['page'])
    

##import json
##response_1 = requests.get("https://api.hh.ru/vacancies/89841853")  #89400788 стандартная вакуха
##full_vacancy_data = response_1.json()
##print()
##print('New:', response_1)
##DICT_Type = dict(full_vacancy_data)
##print(json.dumps(DICT_Type, indent=4, ensure_ascii=False))


#Так проверять в архиве ли вакуха или нет
##response_1 = requests.get("https://api.hh.ru/vacancies/35158775")
##full_vacancy_data = response_1.json()
##print(full_vacancy_data["archived"])
#END Так проверять в архиве ли вакуха или нет
