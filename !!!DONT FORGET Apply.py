import json
"""
A "clumsy " script for tracking where the last commit/PR was made in REMOTE.
It will work if I don't forget to apply it
(I'm not applying the PreCOMMIT yet: I haven't figured out this topic yet)
"""

with open('loc_name.json', 'r') as file:
    loc_name_data = json.load(file)  
    loc_name_value = loc_name_data['locName']  

with open('локация.json', 'r', encoding='utf-8') as File:
    data = json.load(File)
    data["LAST loc"] = loc_name_value

with open('локация.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)
