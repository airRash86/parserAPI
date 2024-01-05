import requests
from SCRIP_For_Clean_Tags import search_TAGS


response_1 = requests.get("https://api.hh.ru/vacancies/88925330")
full_vacancy_data = response_1.json()
print(full_vacancy_data["archived"])
##print(type(full_vacancy_data["description"]))
with open("STORE_descrip.TXT", 'w') as File:
    File.write(full_vacancy_data["description"])

with open("STORE_descrip.TXT") as readFile:
    print(readFile.read())
