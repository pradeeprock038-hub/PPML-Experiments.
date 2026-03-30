'''
write a pandas program to create a dataframe from a dictionary and then transpose
it,ensuring that data types remain consistent.
'''
import pandas as pd
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
transposed_df = df.T
print("\nTransposed DataFrame:")
print(transposed_df)

#.transpose() is used to transpose the DataFrame.
#T is also used to transpose the DataFrame.