import sqlite3
import csv

# 连接到SQLite数据库
conn = sqlite3.connect('data.db')
c = conn.cursor()

# 创建表
table_name = 'lens'
c.execute(f'DROP TABLE IF EXISTS {table_name}')

with open('output.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    columns = next(reader)  # 获取列名
    columns_str = ', '.join([f'"{col}"' for col in columns])
    c.execute(f'CREATE TABLE {table_name} ({columns_str} TEXT)')

    # 插入数据
    insert_query = f'INSERT INTO {table_name} VALUES ({",".join(["?"] * len(columns))})'
    c.executemany(insert_query, reader)

# 提交更改并关闭连接
conn.commit()
conn.close()
