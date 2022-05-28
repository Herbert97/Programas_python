import pandas as pd

miserie = pd.read_csv('edades.csv',header =None, index_col = 0).squeeze(1)
miserie.name = 'Edades'
print(miserie)