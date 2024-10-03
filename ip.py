import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv('music.csv')

df['time'] = df['time'].str.replace(',', '.', regex=True)
# Замена всех NaN на строку 'Nah'
df = df.fillna('Nah')
engine = create_engine('postgresql+psycopg2://postgres:polina08.01@localhost:5432/postgres')

df.columns = df.columns.str.strip()

# Загрузка данных в таблицу 'raw_data' в PostgreSQL
df.to_sql('raw_data', engine, if_exists='replace', index=False)
print(df.columns)
# Сообщение о завершении
print("Data loaded successfully into PostgreSQL.")