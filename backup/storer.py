import pandas as pd

df = pd.read_csv('datos.csv',header=0)

def save(personas_adentro,personas_afuera):
    df = pd.read_csv('datos.csv',header=0)
    #personas_totales = df.loc[2,"Cantidad"]+personas_afuera
    #personas_totales = df.loc[2,"Cantidad"]+personas_afuera
    datos = pd.DataFrame([['entraron', personas_adentro], ['salieron', personas_afuera]], columns=['Tipo', 'Cantidad'])
    datos.to_csv('datos.csv')

def reset():
    datos = pd.read_csv('datos.csv',header=0)
    datos.loc[2,"Cantidad"] = 0
    datos.to_csv('datos.csv')

#save(1,1)
#reset()
#j = df.loc[2,"Cantidad"]
#print(j)