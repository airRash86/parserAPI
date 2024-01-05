import json

# Открытие файла и чтение его содержимого
with open('app_elems.json', 'r') as file:
    data = json.load(file)

    # Вывод содержимого файла целиком
    print("Содержимое файла app_elems.json:")
    print(data)

    # Вывод значения ключа mode
    if 'mode' in data:
        print("Значение ключа 'mode':", data['mode'])
    else:
        print("Ключ 'mode' не найден")

    # Изменение значения ключа mode на 3
    data['mode'] = 3

# Запись изменений обратно в файл
with open('app_elems.json', 'w') as file:
    json.dump(data, file, indent=2)

# Подтверждение изменения
print("Значение ключа 'mode' было изменено на 3")
