import sqlite3
import random

# Создание соединения с базой данных
conn = sqlite3.connect('someDB.db')
cur = conn.cursor()

# Создание таблицы в базе данных (если она еще не существует)
cur.execute('''
    CREATE TABLE IF NOT EXISTS my_one (
        nums INTEGER
    )
''')

# Применение изменений
conn.commit()

# Функция для проверки наличия дубликата в таблице
def is_duplicate(num, cur):
    cur.execute('SELECT COUNT(*) FROM my_one WHERE nums = ?', (num,))
    count = cur.fetchone()[0]
    return count > 0

# Генерация, проверка на дубликаты и вставка 5000 случайных чисел в диапазоне
for _ in range(15000):
    random_num = random.randint(89458375, 89571224)
    while is_duplicate(random_num, cur):
        random_num = random.randint(89458375, 89571224)
    cur.execute('INSERT INTO my_one (nums) VALUES (?)', (random_num,))

# Применение изменений
conn.commit()

# Закрытие соединения
conn.close()
