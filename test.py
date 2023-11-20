import gspread
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/woody/Documents/Python/data/secret_key.json", scopes=scope)

file = gspread.authorize(creds)
workbook = file.open('HS_Statistik_I_Experiment_Daten').sheet1

#access data
#print(workbook.get_all_records)
#print(workbook.row_values(2))

rows = workbook.get_all_values()
print(rows)

df = pd.DataFrame.from_records(rows, columns=['Timestamp','Geschlecht', 'Gewicht in kg', 'Größe in cm','Farbe'])
df1 = df.iloc[1:]
df1['Gewicht in kg'] = df1['Gewicht in kg'].astype(float)
df1['Größe in cm'] = df1['Größe in cm'].astype(float)

#df1 = df.iloc[1:]
#df2 = df1.iloc[:, 2:4].astype(float)
#print(df2)

#df2['Farbe'] = np.where(df2['Geschlecht']!= 'Männlich', 'Red', 'Blue')
#df2.head

df1.plot(kind='scatter', x='Gewicht in kg', y='Größe in cm', c='Farbe', s=50)
"""""
dfs = [test for _, test in df1.groupby('Geschlecht')]
print(dfs[0])
print(dfs[1])


#df2 = df1.iloc[:, 2:4].astype(float)
#print(df2)

#df2.plot.scatter(x='Gewicht in kg',y='Größe in cm',c='Red')

#print(df1)

dtFemale = pd.DataFrame(dfs[1])
dtFemaleFinal = dtFemale.iloc[:, 2:4].astype(float)

dtMale = pd.DataFrame(dfs[0])
dtMaleFinal = dtMale.iloc[:, 2:4].astype(float)
 
#dtFemaleFinal.plot.scatter(x='Gewicht in kg',y='Größe in cm',c= 'Darkred')
#dtMaleFinal.plot.scatter(x='Gewicht in kg',y='Größe in cm',c= 'Darkblue')
"""""

"""

def animate(i):
    rows = workbook.get_all_values()

    df = pd.DataFrame.from_records(rows, columns=['Timestamp','Geschlecht', 'Gewicht in kg', 'Größe in cm'])
    df1 = df.iloc[1:]

    

    dfs = [test for _, test in df1.groupby('Geschlecht')]
    
    dtFemale = pd.DataFrame(dfs[1])
    dtFemaleFinal = dtFemale.iloc[:, 2:4].astype(float)

    dtMale = pd.DataFrame(dfs[0])
    dtMaleFinal = dtMale.iloc[:, 2:4].astype(float) 

    x = dtMaleFinal['Gewicht in kg']
    x1 = dtFemaleFinal['Gewicht in kg']
    y1 = dtMaleFinal['Größe in cm']
    y2 = dtFemaleFinal['Größe in cm']

    plt.cla()

    plt.scatter(x, x1, y1, label='Channel 1')
    plt.scatter(x, x1, y2, label='Channel 2')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)
"""""
plt.show()

