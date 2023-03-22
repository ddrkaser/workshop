import numpy as np
import pandas as pd

gvkey = pd.read_csv(r'compustat identifier2.csv')
drucker = pd.read_csv(r'drucker_cmpsts_match.csv')

drucker2 = drucker.merge(gvkey, on = 'gvkey', how = 'left')
drucker2.to_csv(r'processed_drucker_cmpsts_match.csv',index=False)
