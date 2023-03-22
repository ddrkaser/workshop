import pandas as pd
import numpy as np

df = pd.read_csv(r'hpi.csv')
df.info()
df.describe()
df[['StateCodeFIPS', 'MunicipalCodeFIPS']].dtypes
df.columns

original_cols = list(df.columns)
original_cols.remove('StateName')
original_cols.remove('StateCodeFIPS')
original_cols.remove('MunicipalCodeFIPS')
original_cols.remove('RegionType')
original_cols.remove('FIPS')
original_cols.insert(0,'FIPS')


df['StateCodeFIPS'] = df['StateCodeFIPS'].astype('str')
df['StateCodeFIPS'] = df['StateCodeFIPS'].str.zfill(2)
df['MunicipalCodeFIPS'] = df['MunicipalCodeFIPS'].astype('str')
df['MunicipalCodeFIPS'] = df['MunicipalCodeFIPS'].str.zfill(3)
df['FIPS'] = df['StateCodeFIPS'] + df['MunicipalCodeFIPS']


id_cols = ['FIPS','RegionID', 'SizeRank', 'RegionName','State', 'Metro']
df2 = df[original_cols]

df3 = df2.melt(id_vars=id_cols, var_name="Date", value_name = 'HPI')
df3.to_csv(r'processed_hpi.csv',index=False)
