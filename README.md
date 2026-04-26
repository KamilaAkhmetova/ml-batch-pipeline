# ML Batch Prediction Pipeline

## Project Description

A **batch prediction pipeline** that automatically:
1. Reads input data from PostgreSQL database
2. Applies a trained ML model
3. Stores predictions back to the database
4. Runs automatically on a schedule (every 5 minutes)

## Technologies

- **Python 3.12**
- **PostgreSQL** — database
- **scikit-learn** — ML model
- **joblib** — model loading
- **schedule** — task scheduler

## Setup and Run Instructions

1. Clone the repository
```bash
git clone https://github.com/KamilaAkhmetova/ml-batch-pipeline.git
cd ml-batch-pipeline

2. Install dependencies
pip install -r requirements.txt

3. Configure the database
Create a PostgreSQL database (e.g., ml_pipeline_db).
Create a .env file in the project root:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=ml_pipeline_db
DB_USER=postgres
DB_PASSWORD=your_password

4. Initialize tables and test data
python init_db.py

5. Run the scheduler
python scheduler.py

6. Verify results
SELECT * FROM predictions;