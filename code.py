import pandas as pd
import pandasql as ps

# change path as needed to point at the csv file
path = r'E:\Code\anino_exam_dataeng\AninoDataEngineerExam\dataengineering-test-data.csv'

# copied code
# hash map to store cached dates
# repeating dates are stored in cache in order to improve performance
cache = {}

# changes from string to datetime format in the data frame
def cached_date_parser(s):
    if s in cache:
        return cache[s]
    dt = pd.to_datetime(s, format='%Y%m%d', errors='coerce')
    cache[s] = dt
    return dt

# reads csv file according to path
df = pd.read_csv(path)

# changes install date and event time to datetime values
df['install_date'] = pd.to_datetime(df['install_date'])
df['event_time'] = pd.to_datetime(df['event_time'])

# pandasmysql
# uses SQLite and function is used in order to easily input SQL queries
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
# does not return correct values because pandasql converts win_type_count to int for some reason instead of float
# query still works in SQL
""" query_probability_wintypes = pysqldf('''
    SELECT win_type, (COUNT(*)/ (SELECT COUNT(*) FROM df)) AS win_type_count
    FROM df
    GROUP BY win_type
''')
print("Table of win_types and their respective probabilities: ")
print(query_probability_wintypes) """

""" # pandas code similar to the sql query above but does not have errors
# calculates the COUNT of each 'win_type'
win_type_counts = df['win_type'].value_counts()

# calculate the total number of rows in the DataFrame
total_count = len(df)

# calculate the 'win_type_count' as count of each 'win_type' divided by the total count
result_df = pd.DataFrame({'win_type': win_type_counts.index, 'win_type_count': win_type_counts.values / total_count})

print("Table of win_types and their respective probabilities: ")
print(result_df) """

# Fourth question
# code returns an error due to pandasql but works fine in SQL
""" query_retention = pysqldf('''
    SELECT 
        count_more_than_24_hours / total_count AS retention_rate
    FROM 
    (
        SELECT COUNT(DISTINCT event_user) AS count_more_than_24_hours
        FROM df
        WHERE event_time > install_date + INTERVAL 24 HOUR
    ) AS subquery1
    CROSS JOIN 
    (
        SELECT COUNT(DISTINCT event_user) AS total_count
        FROM df
    ) AS subquery2
''')

print(query_retention['retention_rate'][0]) """

""" # pandas code that returns the same result as the SQL query
# Calculate count_more_than_24_hours by filtering the data frame of those that have spun since the 24 hour mark
filtered_data = df[df['event_time'] > df['install_date'] + pd.Timedelta(hours=24)]
# only take unique users
count_more_than_24_hours = filtered_data['event_user'].nunique()

# calculate unique users
total_count = df['event_user'].nunique()

# Calculate retention_rate
retention_rate = (count_more_than_24_hours / total_count) * 100

print("The retention rate of the game is: " + str(retention_rate)) """

# Fifth question
# code below does not work due to pandasql having operational errors
# works fine in mySQL
""" query_avg_rtp = pysqldf('''
    SELECT 
        slotmachine_id, AVG(rtp) AS avg_rtp
    FROM
        (SELECT 
            slotmachine_id,
                amount / total_bet_amount AS rtp
        FROM
            game_data
        ) AS summary
    GROUP BY
        slotmachine_id
''')
print("Average RTP for each slot machine: ")
print(query_avg_rtp)"""

# converted mySQL query into similar pandas code
""" df['rtp'] = df['amount'] / df['total_bet_amount']

# Group by 'slotmachine_id' and calculates the average 'rtp' per slotmachine_id
summary_df = df.groupby('slotmachine_id')['rtp'].mean().reset_index()

# Rename the 'rtp' column to 'avg_rtp'
summary_df.rename(columns={'rtp': 'avg_rtp'}, inplace=True)

print(summary_df) """