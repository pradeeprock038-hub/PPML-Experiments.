#2.convert mixed type series to detetime and filter invalid dates.

import pandas as pd
s = pd.Series(['2023-01-01','not a date','2024-o5-10'])
dt_s = pd.to_datetime(s,errors = 'coerce')
valid_dates = dt_s.dropna()
print(valid_dates)