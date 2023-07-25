import pandas as pd
import pandasql as ps

path = r'E:\Code\anino_exam_dataeng\AninoDataEngineerExam\dataengineering-test-data.csv'

cache = {}

def cached_date_parser(s):
    if s in cache:
        return cache[s]
    dt = pd.to_datetime(s, format='%Y%m%d', errors='coerce')
    cache[s] = dt
    return dt
    
df = pd.read_csv(path)
df['install_date'] = pd.to_datetime(df['install_date'])
df['event_time'] = pd.to_datetime(df['event_time'])

print(df.shape)
print(df.dtypes)

pysqldf = lambda q: ps.sqldf(q, globals())

print(pysqldf('''
    SELECT COUNT(DISTINCT event_user)
   FROM df
'''))