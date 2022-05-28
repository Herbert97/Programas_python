import pandas as pd
edades = {"Juan":40, "Pedro":20, "Maria":36, "Francisco":20, "Luis":34}
datos = pd.Series(edades)
datos.name = 'Edades'

# edad Pedro
print( datos['Pedro'], '\n' )

# los primeros tres (Juan, Pedro, Maria)
print( datos[:'Maria'], '\n' )

# los ultimos tres (Maria, Francisco, Luis)
print( datos['Maria':], '\n' )

# elementos consecutivos(desde Juan hasta Maria)
print( datos['Juan':'Maria'] ,'\n')

# elementos no consecurivos(Juan y Maria)
print( datos[['Juan','Maria']], '\n' )