# write a pandas program to merge two dataframes on a common column and then sort the resulting dataframe by a specific column.
import pandas as pd
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [1, 2, 3], 'Age': [25, 30, 35]})
merged_df = pd.merge(df1, df2, on='ID')
sorted_df = merged_df.sort_values(by='Age')
print(sorted_df)

