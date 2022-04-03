import pandas as pd
from pandas_profiling import ProfileReport
data = "C:/Users/Omomule Taiwo G/Desktop/phd_datasets/sonar_all_data.csv"
df = pd.read_csv(data, delimiter=',', header=None)
df = df.iloc[0:200]
print(df)
#Inspect data
print("R^2 Score:",df.shape)
gen_report = ProfileReport(df, title='Sonar Report')
print(gen_report)
