##import sqlite3
### Устанавливаем соединение с базой данных (если нет, то она будет автоматически создана)
##conn = sqlite3.connect('bigDB.db')
### Создаем курсор для работы с базой данных
##cur = conn.cursor()
### Создаем таблицу nums_scanned_vacancies с колонкой nums
##cur.execute('''CREATE TABLE IF NOT EXISTS nums_scanned_vacancies (
##               nums INTEGER)''')
##
### Завершаем транзакцию и сохраняем изменения в базе данных
##conn.commit()
### Закрываем соединение с базой данных
##conn.close()
##print("База данных bigDB.db с таблицей nums_scanned_vacancies была успешно создана")

####----------------------

##import sqlite3
### Функция для вывода всех значений из поля nums
##def select_all_from_table():
##    conn = sqlite3.connect('bigDB.db')
##    cur = conn.cursor()
##
##    # Выбираем все значения из поля nums
##    cur.execute("SELECT nums FROM nums_scanned_vacancies")
##    rows = cur.fetchall()
##
##    print("Все значения из поля nums:")
##    for row in rows:
##        print(row[0])
##
##    conn.close()
##
### Функция для вставки новых значений в колонку nums
##def insert_values_into_table(values):
##    conn = sqlite3.connect('bigDB.db')
##    cur = conn.cursor()
##
##    # Вставляем новые значения
##    for value in values:
##        cur.execute("INSERT INTO nums_scanned_vacancies (nums) VALUES (?)", (value,))
##
##    # Сохраняем изменения
##    conn.commit()
##    conn.close()
### Выводим все значения из поля nums
##select_all_from_table()
### Новые значения для вставки
##new_values = [35, 80, 'u997']
### Вставляем новые значения в колонку nums
##insert_values_into_table(new_values)
### Подтверждение вставки
##print("Новые значения были успешно добавлены в колонку nums")

###---------------------------

import sqlite3

# Функция для добавления новой колонки в таблицу
def add_new_column():
    conn = sqlite3.connect('bigDB.db')
    cur = conn.cursor()

    # Выполнение SQL-запроса для добавления новой колонки
    cur.execute("ALTER TABLE nums_scanned_vacancies ADD COLUMN descr_vac TEXT")

    # Сохраняем изменения
    conn.commit()
    conn.close()

    print("Новая колонка descr_vac была успешно добавлена в таблицу nums_scanned_vacancies")

# Вызываем функцию для добавления новой колонки
add_new_column()



