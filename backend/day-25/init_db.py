import sqlite3

conn = sqlite3.connect(r"C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-25\books.db")

with open(r"C:\Users\johng\Documents\.College\AWS\AWSCC-CodeQuest-Backend\backend\day-25\schema.sql") as f:
    conn.executescript(f.read())

cur = conn.cursor()

cur.execute('''
            INSERT INTO books (title, author, published_year) 
            VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960);
            ''')

conn.commit()
conn.close()