import schedule
import time
import subprocess
import datetime

def run_prediction():
    print(f"\n[{datetime.datetime.now()}] Запуск предсказаний...")
    try:
        result = subprocess.run(
            ["python", "predict.py"],
            capture_output=True,
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode == 0:
            print(f"[{datetime.datetime.now()}] ✅ {result.stdout}")
        else:
            print(f"[{datetime.datetime.now()}] ❌ Ошибка: {result.stderr}")
            
    except Exception as e:
        print(f"[{datetime.datetime.now()}] ❌ Исключение: {e}")

schedule.every(5).minutes.do(run_prediction)  


print("🕐 Планировщик запущен. Будет выполнять предсказания каждые 5 минут.")
print("Для остановки нажмите Ctrl+C\n")

run_prediction()

while True:
    schedule.run_pending()
    time.sleep(1) 