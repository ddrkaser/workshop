import pandas as pd
import numpy as np

df = pd.read_csv(r'Unemployment.csv')
df.info()
df.describe()
df[['StateCodeFIPS', 'MunicipalCodeFIPS']].dtypes
df.columns

cols=['FIPS_code','State','Area_name','Rural_urban_continuum_code_2013','Urban_influence_code_2013','Metro_2013','Unemployment_rate_2000','Unemployment_rate_2001','Unemployment_rate_2002','Unemployment_rate_2003','Unemployment_rate_2004','Unemployment_rate_2005','Unemployment_rate_2006','Unemployment_rate_2007','Unemployment_rate_2008','Unemployment_rate_2009','Unemployment_rate_2010','Unemployment_rate_2011','Unemployment_rate_2012','Unemployment_rate_2013','Unemployment_rate_2014','Unemployment_rate_2015','Unemployment_rate_2016','Unemployment_rate_2017','Unemployment_rate_2018','Unemployment_rate_2019','Unemployment_rate_2020','Unemployment_rate_2021']

df2 = df[cols]
df2['FIPS_code'] = df2['FIPS_code'].astype('str')
df2['FIPS_code'] = df2['FIPS_code'].str.zfill(5)

id_cols=['FIPS_code','State','Area_name','Rural_urban_continuum_code_2013','Urban_influence_code_2013','Metro_2013']

df3 = df2.melt(id_vars=id_cols, var_name="Year", value_name = 'Unemployment_rate')

df3['Year'] = df3['Year'].str.extract(r'\_(\d*)$')
df3.to_csv(r'processed_unemployment.csv',index=False)
