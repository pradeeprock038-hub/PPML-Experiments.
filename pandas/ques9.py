'''
write a pandas program to split the following dataframe into groups based on school
code.Also check the type of groupby object.

'''
import pandas as pd
pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
data = {
    'school_code': ['001', '002', '001', '002', '001', '002'],
    'student_name': ['pradeep', 'tarun', 'sai', 'naveen', 'kodi', 'ram'],
    'grade': [85, 90, 78, 92, 88, 95],
    'class' : ['A', 'B', 'A', 'B', 'A', 'B']
}
students_df = pd.DataFrame(data)
result = students_df.groupby('school_code')
for name,group in result:
    print("\nGroup")
    print(name)
    print(group)
print("\nType of groupby object:")
print(type(result))

          