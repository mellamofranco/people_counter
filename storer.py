import pandas as pd

df = pd.read_csv('datos.csv',header=0)

def save(personas_adentro,personas_afuera):
    df = pd.read_csv('datos.csv',header=0)
    personas_totales = df.loc[2,"Cantidad"]+personas_adentro
    datos = pd.DataFrame([['personas adentro', personas_adentro], ['personas afuera', personas_afuera],['personas totales', personas_totales]], columns=['Tipo', 'Cantidad'])
    datos.to_csv('datos.csv')

def reset():
    datos = pd.read_csv('datos.csv',header=0)
    datos.loc[2,"Cantidad"] = 0
    datos.to_csv('datos.csv')

#save(0,0)
#reset()
j = df.loc[2,"Cantidad"]
print(j)