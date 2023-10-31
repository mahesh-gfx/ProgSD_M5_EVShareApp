import sqlite3
import random
import datetime

# generate fake data order
conn = sqlite3.connect('zevo-dev.db')
cursor = conn.cursor()
# 随机选择一个用户名
for i in range(10000):
    print(i)
    cursor.execute("SELECT username FROM users ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    if result:
        username = result[0]

    # 生成随机的startTime和endTime
    current_time = datetime.datetime.now()
    one_year_ago = current_time - datetime.timedelta(days=365)
    start_time = one_year_ago + datetime.timedelta(seconds=random.randint(0, 31536000))
    end_time = start_time + datetime.timedelta(seconds=random.randint(1, 86400))

    # 生成随机的income
    income = str(random.randint(10, 100))

    # 插入数据到orders表
    cursor.execute("INSERT INTO orders (username, startTime, endTime, income) VALUES (?, ?, ?, ?)",
                   (username, start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'), income))

    # 提交更改并关闭连接
    conn.commit()
conn.close()