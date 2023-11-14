# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


df_list = []
# Dataset:
a = pd.DataFrame({ 'group' : np.repeat('A',500), 'value': np.random.normal(13, 1.2, 500) })
b = pd.DataFrame({ 'group' : np.repeat('B',500), 'value': np.random.normal(13, 1.2, 500) })
c = pd.DataFrame({ 'group' : np.repeat('C',500), 'value': np.random.normal(18, 1.2, 500) })
d = pd.DataFrame({ 'group' : np.repeat('D',20), 'value': np.random.normal(25, 4, 20) })
e = pd.DataFrame({ 'group' : np.repeat('E',100), 'value': np.random.uniform(12, size=100) })
print(e)
df_list.append(a)
df_list.append(b)
df_list.append(c)
df_list.append(d)
df_list.append(e)

final_df = pd.concat(df_list)

# boxplot
ax = sns.boxplot(x='group', y='value', data=final_df)

# violin plot - andere Form des Boxplot
#ax = sns.violinplot(x='group', y='value', data=df)

# add stripplot - kann auskommentiert werden - nur zur Darstellungszwecke
ax = sns.stripplot(x='group', y='value', data=final_df, color="orange", jitter=0.2, size=2.5)

# add title
plt.title("Boxplot Beispiel", loc="center")

plt.autoscale

# show the graph
plt.show()