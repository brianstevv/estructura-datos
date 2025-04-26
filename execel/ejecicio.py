import pandas as pd

class Hospital:
    def __init__(self,nombre:str,nit:int,municipio:str,sede;str):
        self.nombre=nombre
        self.nit=nit
        self.municipio=municipio
        self.sede=sede

    def __str__(self):
        return f"Nombre:{self.nombre},nit{self.nit},municipio {self.municipio},sede{self.sede}"

class Nodo:
    def __init__(self,hospital):
        self.hospital=hospital
        self.izquierda=None
        self.derecha=None

#cargar el archivo csv
hospitales = pd.read_csv('/workspaces/estructura-datos/execel/directorio.csv')
#print(hospitales.head())

hospitales.rename(columns={
    'Razón Social Organización':'Razón Social Organización',
    'Número NIT':'Número NIT',
    'NIT':'NIT',
    'Sede':'Sede',
    'Municipio':'Municipio'

}, inplace=True)

hospitales['Número NIT']=hospitales['Número NIT'].str.replace(',','',)
hospitales['NIT']=hospitales['NIT'].astype(int)
print(hospitales.head())
print(hospitales.columns)
print(hospitales['Número NIT'])

for index, row in hospitales.iterrows():
    hospital=Hospital(
        nombre=row['Razón Social Organización'],
        nit=row['NIT'],
        sede=row['Sede'],
        municipio=row['Municipio'],
    )
    print(hospital)


