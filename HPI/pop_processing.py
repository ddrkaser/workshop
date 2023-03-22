import pandas as pd
import numpy as np

file = open('county_pop.txt', 'r')
pop_data = file.readlines()
file.close()

######
race = {
    "1": "White",
    "2": "Black",
    "3": "American Indian/Alaska Native",
    "4": "Asian or Pacific Islander"
}

origin = {
    "0": "Non-Hispanic",
    "1": "Hispanic",
    "9": "Not applicable"
}

sex = {
    "1": "Male",
    "2": "Female"
}

age_group = {
    "00": "Age 00",
    "01": "Ages 01-04",
    "02": "Ages 05-09",
    "03": "Ages 10-14",
    "04": "Ages 15-19",
    "05": "Ages 20-24",
    "06": "Ages 25-29",
    "07": "Ages 30-34",
    "08": "Ages 35-39",
    "09": "Ages 40-44",
    "10": "Ages 45-49",
    "11": "Ages 50-54",
    "12": "Ages 55-59",
    "13": "Ages 60-64",
    "14": "Ages 65-69",
    "15": "Ages 70-74",
    "16": "Ages 75-79",
    "17": "Ages 80-84",
    "18": "Ages 85+",
    "99": "Unknown Age"
}

county_pop = []

for data in pop_data:
    record = {"Year": data[0:4],
              "State": data[4:6],
              "FIPS": data[6:11],
              "Race": race.get(data[13:14], "N/A"),
              "Origin": origin.get(data[14:15], "N/A"),
              "Sex": sex.get(data[15:16], "N/A"),
              "Age": age_group.get(data[16:18], "N/A"),
              "Population": data[18:26]}
    county_pop.append(record)

df = pd.DataFrame(county_pop)
df.to_csv(r'county_pop.csv',index=False)

df_01001 = df[df['FIPS'] == '01001']
df_01001_2000 = df_01001[df_01001['Year'] == '2000']


df['Population'] = df['Population'].astype('int')
df2 = df.groupby(['FIPS','Year']).agg(
    Total_population=("Population", "sum")
)

df3 = df.groupby(['State','FIPS','Year']).agg(
    Total_population=("Population", "sum")
).reset_index()

df3['FIPS'] = df3['FIPS'].astype('str')
df3['FIPS'] = df3['FIPS'].str.zfill(5)

df3.to_csv(r'county_pop.csv',index=False)
