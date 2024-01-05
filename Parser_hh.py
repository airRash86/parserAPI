import requests

def get_vacancies(programming_language, experience='no-experience', count=50,\
                  p=None):
    url = 'https://api.hh.ru/vacancies'
    params = {'text': f'программист {programming_language}',
              'area': 1,
              'experience': experience,
              'per_page': count}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        print('Пагинация: ', response.json()['page'])
        vacancies = data.get('items', [])
        return vacancies
    else:
        print(f'Ошибка при получении вакансий: {response.status_code}')

programming_language = 'Python'
##for vacancy in vacancies:
##    print(vacancy['name'])

def loop_on_resp(vacancies):
    c=1
    for vacancy in vacancies:
        print(vacancy['id'])
##        if c ==1:
##            print(vacancy)   
        c +=1
    print('Счетчик:', c)
vacancies = get_vacancies(programming_language, experience='noExperience', count=100)
loop_on_resp(vacancies)





##-----------------



##-----------------

###-------------------
##import requests
##
##import json
##import time
##
##import os
##
## 
##def getPage(page = 0):
##    """
##    Создаем метод для получения страницы со списком вакансий.
##    Аргументы:
##        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
##    """
##    
##    # Справочник для параметров GET-запроса
##    params = {
##        'text': 'NAME:Аналитик', # Текст фильтра. В имени должно быть слово "Аналитик"
##        'area': 1, # Поиск ощуществляется по вакансиям города Москва
##        'page': page, # Индекс страницы поиска на HH
##        'per_page': 25 # Кол-во вакансий на 1 странице
##    }
##    
##    
##    req = requests.get('https://api.hh.ru/vacancies') #, params) # Посылаем запрос к API
##    data = req.content.decode() # Декодируем его ответ, чтобы Кириллица отображалась корректно
##    req.close()
##    return data
##print(json.loads(getPage(page = 0))["items"][0])
####c = 1
####for i in a:
####    c +=1
####print(c)
    
###-------------------
### Считываем первые 2000 вакансий
##for page in range(0, 20):
##    
##    # Преобразуем текст ответа запроса в справочник Python
##    jsObj = json.loads(getPage(page))
##    
##    # Сохраняем файлы в папку {путь до текущего документа со скриптом}\docs\pagination
##    # Определяем количество файлов в папке для сохранения документа с ответом запроса
##    # Полученное значение используем для формирования имени документа
##    nextFileName = './docs/pagination/{}.json'.format(len(os.listdir('./docs/pagination')))
##    
##    # Создаем новый документ, записываем в него ответ запроса, после закрываем
##    f = open(nextFileName, mode='w', encoding='utf8')
##    f.write(json.dumps(jsObj, ensure_ascii=False))
##    f.close()
##    
##    # Проверка на последнюю страницу, если вакансий меньше 2000
##    if (jsObj['pages'] - page) <= 1:
##        break
##    
##    # Необязательная задержка, но чтобы не нагружать сервисы hh, оставим. 5 сек мы может подождать
##    time.sleep(0.25)
##    
##print('Старницы поиска собраны')
##После получения страниц со списком вакансий получим детальную информацию по каждой вакансии. Для этого разберем JSON в полученных документах и для каждой вакансии обратимся к API по готовой ссылке https://api.hh.ru/vacancies/{id вакансии}?host=hh.ru.
##
##Пример json-данных со списком вакансий
##Результатом работы следующего скрипта будет являться папка vacancies, наполненная файлами с информацией по вакансиям:
##
##import json
##import os
##import requests
##import time
##
### Получаем перечень ранее созданных файлов со списком вакансий и проходимся по нему в цикле 
##for fl in os.listdir('./docs/pagination'):
##    
##    # Открываем файл, читаем его содержимое, закрываем файл
##    f = open('./docs/pagination/{}'.format(fl), encoding='utf8')
##    jsonText = f.read()
##    f.close()
##    
##    # Преобразуем полученный текст в объект справочника
##    jsonObj = json.loads(jsonText)
##    
##    # Получаем и проходимся по непосредственно списку вакансий
##    for v in jsonObj['items']:
##        
##        # Обращаемся к API и получаем детальную информацию по конкретной вакансии
##        req = requests.get(v['url'])
##        data = req.content.decode()
##        req.close()
##        
##        # Создаем файл в формате json с идентификатором вакансии в качестве названия
##        # Записываем в него ответ запроса и закрываем файл
##        fileName = './docs/vacancies/{}.json'.format(v['id'])
##        f = open(fileName, mode='w', encoding='utf8')
##        f.write(data)
##        f.close()
##        
##        time.sleep(0.25)
##        
##print('Вакансии собраны')
