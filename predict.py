import psycopg2
import joblib  
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host=os.getenv("DB_HOST", "localhost"),
    database=os.getenv("DB_NAME", "ml_pipeline_db"),
    user=os.getenv("DB_USER", "postgres"),
    password=os.getenv("DB_PASSWORD")
)
cursor = conn.cursor()

model = joblib.load("model.joblib")

cursor.execute("SELECT id, duration, amount, age FROM input_data")
rows = cursor.fetchall()

for row in rows:
    features = [[row[1], row[2], row[3]]] 
    prediction = model.predict(features)[0]
    
    cursor.execute("""
        INSERT INTO predictions (id, prediction, prediction_timestamp)
        VALUES (%s, %s, NOW())
    """, (row[0], float(prediction)))

conn.commit()
cursor.close()
conn.close()
print("✅ Предсказания сохранены!")