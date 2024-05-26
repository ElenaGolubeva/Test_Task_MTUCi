from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

# Модель данных для списка слов
class WordsModel(BaseModel):
    words: list

app = FastAPI()

# Подключение к PostgreSQL
conn = psycopg2.connect(
    host="postgres",
    database="wordsdb",
    user="lena",
    password="mypassword"
)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS words (
        id SERIAL PRIMARY KEY,
        word TEXT
    )
""")
conn.commit()

@app.post("/data")
def create_data(data: WordsModel):
    for item in data.words:
        cursor.execute("INSERT INTO words (word) VALUES (%s)", (item,))
        conn.commit()
    return {"Status": "OK"}
    
    
    '''
    cursor.execute("Select * FROM data")
    rows = cursor.fetchall()

    # Вывод результата в консоль
    for row in rows:
        print(row)

    '''

