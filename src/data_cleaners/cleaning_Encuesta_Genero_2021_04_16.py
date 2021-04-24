import pandas as pd
from helpers import clean_database

df1 = pd.read_excel('data\\crudos\\2021 04 16 Encuesta_género_mentores.xlsx')
df2 = pd.read_excel('data\\crudos\\2021 04 16 Encuesta_género_mentores.xlsx',
                    sheet_name=1)
df1['Momento'] = 'Antes de las 10'
df2['Momento'] = 'Despues de las 10'

df = df1.append(df2, ignore_index=True)


# 'Sexo'
# 'Departamento de residencia' -> Cambiar a 'Departamento'
# 'Municipio de residencia' -> Cambiar a 'Municipio'
# 'Estrato socio-económico' -> Cambiar a 'Estrato'
# 'Pertenece a algún grupo étnico' -> Borrar y cambiar 'Grupo étnico al que pertenece' por 'Grupo étnico'
# 'Nivel de formación
# 'Profesión'

df = df.drop(columns=['¿Pertenece a algún grupo étnico?'])
df = df.rename(columns={
    'Departamento de residencia': 'Departamento',
    'Municipio de residencia': 'Municipio',
    'Estrato socio-económico': 'Estrato',
    'Grupo étnico al que pertenece': 'Grupo étnico'
})
df.columns = df.columns.str.replace(
    'Por favor, evalúe los enunciados de acuerdo con su experiencia, según la siguiente escala',
    "Según su experiencia:"
)
df['Grupo étnico'] = df['Grupo étnico'].fillna('Ninguno')
df = df.drop_duplicates(subset=["Correo electrónico"], keep='first')

options = {
    'Fecha de nacimiento': 'dob',
    'Profesión': 'profesion',
    'Municipio': 'municipio'
}

df = clean_database(df, options=options)


df.to_excel("data\\limpios\\Encuesta_Genero_Limpia_2021_04_16.xlsx")
