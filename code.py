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

pysqldf = lambda q: ps.sqldf(q, globals())

# First question

""" query_uniqueplayers = pysqldf('''
    SELECT COUNT(DISTINCT event_user) as distinct_users
    FROM df
''')

print("Unique players in the data: " + str(query_uniqueplayers['distinct_users'][0])) """

# Second question
""" # A
query_sessionslots = pysqldf('''
    SELECT AVG(number_of_slot_machines) AS average_number_of_slot_machines
    FROM (
        SELECT session_id, COUNT(DISTINCT session_token) AS number_of_slot_machines
        FROM df
        GROUP BY session_id
    )
''')

print("Average number of slot machines a player plays in a session: " + str(query_sessionslots['average_number_of_slot_machines'][0]))

# B
query_sessionspins = pysqldf('''
    SELECT AVG(spins_count) AS average_spins_count
    FROM (
        SELECT session_token, COUNT(*) AS spins_count
        FROM df
        GROUP BY session_token
    )
''')

print("Average number of spins per machine session: " + str(query_sessionspins['average_spins_count'][0])) """

# Third question
# does not work because pandasql converts win_type_count to int for some reason instead of float
# query still works in SQL
""" query_probability_wintypes = pysqldf('''
    SELECT win_type, (COUNT(*)/ (SELECT COUNT(*) FROM df)) AS win_type_count
    FROM df
    GROUP BY win_type
''')
print("Table of win_types and their respective probabilities: ")
print(query_probability_wintypes) """