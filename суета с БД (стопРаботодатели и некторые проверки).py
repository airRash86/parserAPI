import sqlite3

### Устанавливаем соединение с базой данных
##conn = sqlite3.connect('DBbigForNumsAndOthers.db')
##
### Создаем курсор для выполнения операций с базой данных
##cursor = conn.cursor()
##
### Создаем таблицу stoppedEmployers
##cursor.execute('''
##    CREATE TABLE IF NOT EXISTS stoppedEmployers (
##        namesStoppedEmployers TEXT
##    )
##''')
##
### Сохраняем изменения и закрываем соединение
##conn.commit()
##conn.close()

STR = ['ВижнЛабс (VisionLabs)', 'SberTech', 'Банк Открытие', 'ХОУМ Банк', 'СберМедИИ', 'Кухня на районе', 'ВкусВилл', 'СберМаркет', 'СБЕР', 'Альфа-Банк', 'РОСБАНК',
       'Почта Банк', 'ПСБ (ПАО «Промсвязьбанк»)', 'Банк ДОМ.РФ', 'Газпромбанк', 'РНКБ Банк (ПАО)',  'Банк ВТБ (ПАО)', 'Тинькофф', 'СберСпасибо', 'МСП Банк',
       'БАНК УРАЛСИБ', 'Московская Биржа', 'Райффайзен Банк', 'Вкусно — и точка', 'SberAutoTech', 'Московский Кредитный Банк', 'Центральный банк Российской Федерации',
       'Finstar Financial Group', 'Ренессанс cтрахование, Группа', 'ФинГрад', 'Ингосстрах Банк', 'Красное & Белое, розничная сеть', 'Россельхозбанк', 'ОТП Банк, АО (OTP bank)',
       'СберЗдоровье', 'CarMoney', 'МТС Финтех', 'Бэнкс Софт Системс']



conn = sqlite3.connect('DBbigForNumsAndOthers.db')

# Создаем курсор для выполнения операций с базой данных
cursor = conn.cursor()

# Проходим по каждому элементу списка и вносим его в таблицу
for employer in STR:
    # Приводим элемент к нижнему регистру
    lowered_employer = employer.lower()
    # Используем SQL-запрос для вставки данных в таблицу
    cursor.execute('INSERT INTO stoppedEmployers (namesStoppedEmployers) VALUES (?)', (lowered_employer,))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
