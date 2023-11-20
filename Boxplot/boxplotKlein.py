import seaborn as sns

import matplotlib.pyplot as plt

# Example data
data = {'Reihen': ['Reihe 1', 'Reihe 1', 'Reihe 1', 'Reihe 2', 'Reihe 2', 'Reihe 2'],
        'Alter': [20, 18,30, 31, 26, 22]}

# Create a boxplot
sns.boxplot(x='Reihen', y='Alter', data=data)

#Einzelne Punkte als Beispiel anzeigen - Kann auskommentiert werden
ax = sns.stripplot(x='Reihen', y='Alter', data=data, color="orange", jitter=0.2, size=8)


# Display the plot
plt.show()