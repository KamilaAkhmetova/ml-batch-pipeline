import psycopg2
# from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", 5432),
    "database": os.getenv("DB_NAME", "ml_pipeline_db"),
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD")  
}

def create_tables():    
    print("Подключение к базе данных...")
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS input_data (
        id SERIAL PRIMARY KEY,
        duration FLOAT,
        amount FLOAT,
        age FLOAT
    );
    """)
    print("✓ Таблица 'input_data' создана (или уже существует)")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        prediction FLOAT,
        prediction_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)
    print("✓ Таблица 'predictions' создана (или уже существует)")
    
    cursor.execute("SELECT COUNT(*) FROM input_data")
    count = cursor.fetchone()[0]
    
    if count == 0:
        print("\nДобавление тестовых данных...")
        cursor.execute("""
        INSERT INTO input_data (duration, amount, age) VALUES
        (12.5, 1000.0, 25.0),
        (24.0, 2500.0, 35.0),
        (6.0, 500.0, 45.0),
        (18.0, 3000.0, 28.0),
        (30.0, 1500.0, 52.0);
        """)
        print("✓ Добавлено 5 тестовых записей")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print("\n✅ База данных готова к работе!")

if __name__ == "__main__":
    create_tables()