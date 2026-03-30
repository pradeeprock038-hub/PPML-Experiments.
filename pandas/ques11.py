'''
create a sample dataframe with 'year' and 'sales' columns.
use plt.plot() to plot 'year' vs 'sales'.
Add axis labels and a title to the plot using plt.xlabel(), plt.ylabel(), and plt.title().
Display the plot using plt.show(). 
'''
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'year': [2015, 2016, 2017, 2018, 2019],
    'sales': [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)
plt.plot(df['year'], df['sales'], marker='o')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Yearly Sales')
plt.grid()
plt.show()
