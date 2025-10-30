import pandas as pd
from sqlalchemy import create_engine
import datetime as dt

# Connect to PostgreSQL
engine = create_engine("postgresql://admin:admin@postgres:5432/salesdb")

# Extract data
df = pd.read_sql("SELECT * FROM employees", engine)

# Transformations
df['full_name'] = df['full_name'].str.title()
df['yearly_salary'] = df['monthly_salary'] * 12
today = pd.Timestamp.now()
df['experience_years'] = (today.year - pd.to_datetime(df['hire_date']).dt.year)
df['salary_grade'] = df['monthly_salary'].apply(lambda x: 'A' if x > 9000 else 'B' if x > 7000 else 'C')

# Load to new table
df.to_sql("employees_cleaned", engine, if_exists="replace", index=False)

print("ETL Job Completed Successfully ✅")

