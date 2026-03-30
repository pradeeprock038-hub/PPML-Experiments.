import pandas as pd 
s = pd.Series(['10','20','abc',30])
numaric_s= pd.to_numeric(s,errors='coerce')
print(numaric_s)

'''
Note:errors='coerce
this is the key concept *
if conversion is possible >> convert normally
if conversion fails >> replaces with NaN(Not a Number)
'''

