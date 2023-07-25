import pandas as pd
import pandasql as ps

path = r'E:\Code\anino_exam_dataeng\AninoDataEngineerExam\dataengineering-test-data.csv'

df = pd.read_csv(path)

print(df.shape)