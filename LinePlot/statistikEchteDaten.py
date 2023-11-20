import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stat

data = pd.read_excel('Netflix Revenue and Usage Statistics.xlsx', sheet_name=0)


x = data['Year']
y1 = data['Revenue ($bn)']    

plt.cla()
plt.bar(x, y1, label='Netlfix Umsatz in Milliarden Dollar')


plt.legend(loc='upper left')
plt.autoscale()

# Display the plot
plt.show()

###########
data = pd.read_excel('Netflix Revenue and Usage Statistics.xlsx', sheet_name=5)


x = data['Date']
y1 = data['Subscribers (mm)']    

plt.cla()

plt.plot(x.sort_values(), y1, label='Netflix Subscriber in Millionen')

plt.legend(loc='upper left')
plt.autoscale()

# Display the plot
plt.show()