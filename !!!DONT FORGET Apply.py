import json

with open('loc_name.TXT', 'r', encoding='utf-8') as File:
    loc_name_value = File.readline().strip()  

with open('локация.json', 'r', encoding='utf-8') as File:
    data = json.load(File)
    data["LAST loc"] = loc_name_value

with open('локация.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
