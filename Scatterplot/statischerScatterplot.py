import gspread
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/Users/woody/Documents/GitHub/Statistik/data/secret_key.json", scopes=scope)

file = gspread.authorize(creds)

workbook = file.open('HS_Statistik_I_Experiment_Daten').sheet1
rows = workbook.get_all_values()

print(rows)

df = pd.DataFrame.from_records(rows, columns=['Timestamp','Geschlecht', 'Gewicht in kg', 'Größe in cm'])
df1 = df.iloc[1:]

df1['Gewicht in kg'] = df1['Gewicht in kg'].astype(float)
df1['Größe in cm'] = df1['Größe in cm'].astype(float)
df1['Farbe'] = np.where(df1['Geschlecht']!= 'Männlich', 'Red', 'Blue')
df1.head
df1.plot(kind='scatter', x='Gewicht in kg', y='Größe in cm', c='Farbe', s=50)

plt.show()

