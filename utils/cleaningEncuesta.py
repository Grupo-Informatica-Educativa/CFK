import pandas as pd
from diccionario import similitudes
from unidecode import unidecode

encuesta = pd.read_excel("data/crudos/2021 04 16 Encuesta_género_mentores.xlsx")

# Vamos a concentrarnos en aquellas columnas que son categorizables y analizarlas

# 'Sexo'
# 'Departamento de residencia' -> Cambiar a 'Departamento'
# 'Municipio de residencia' -> Cambiar a 'Municipio'
# 'Estrato socio-económico' -> Cambiar a 'Estrato'
# 'Pertenece a algún grupo étnico' -> Borrar y cambiar 'Grupo étnico al que pertenece' por 'Grupo étnico'
# 'Nivel de formación
# 'Profesión'

encuesta = encuesta.drop(columns=['¿Pertenece a algún grupo étnico?'])
encuesta = encuesta.rename(columns={
    'Departamento de residencia': 'Departamento',
    'Municipio de residencia' : 'Municipio',
    'Estrato socio-económico' : 'Estrato',
    'Grupo étnico al que pertenece' : 'Grupo étnico'
})
encuesta['Grupo étnico'] = encuesta['Grupo étnico'].fillna('Ninguno')

datos = encuesta[['Sexo', 'Departamento', 'Municipio', 'Estrato','Grupo étnico', 'Nivel de formación', 'Profesión']]

# Limpiando valores

# Lidian con municipios the easy way
def remplazar_municipios(municipio):
    municipio = unidecode(municipio.strip().lower())
    return (similitudes[municipio]  if municipio in similitudes else municipio)

datos['Municipio'] =  datos['Municipio'].map(lambda val: remplazar_municipios(val))

# Lidiando con profesiones

ingenierias = {'sistema': 'de sistemas','electro': 'electronica','informatic': 'informatica','industrial': 'industrial','telecom' : 'de telecomunicaciones'}
def remplazar_profesiones(profesion):
    profesion = unidecode(profesion.strip().lower())
    if 'ing' in profesion:
        for ing in ingenierias:
            if ing in profesion:
                return 'ingenieria '+ingenierias[ing]
        
    return profesion

datos['Profesión'] =  datos['Profesión'].map(lambda val: remplazar_profesiones(val))

print(datos['Profesión'].unique())