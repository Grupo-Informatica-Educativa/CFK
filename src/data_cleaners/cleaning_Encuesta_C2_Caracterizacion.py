
import pandas as pd

save_new = True

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

def add_columns(df1, df2):
    for col in df2.columns:
        df1[col] = df2[col]

##################################################################################

df_inicial = pd.read_csv('data/crudos/Inicial.csv',
                         error_bad_lines=False, 
                         warn_bad_lines=False,
                         low_memory=False)
df_inicial["Pregunta"] = df_inicial["Pregunta"].str.replace("\n", " ").replace("\b", " ")
_items = df_inicial[df_inicial["Pregunta"] == "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia: "]["Respuesta"]
_items = _items.str.contains("TIC")
df_inicial["temp"] = _items.copy()
df_inicial["temp"] = df_inicial["temp"].fillna(False)
df_inicial.loc[df_inicial["temp"],"Pregunta"] = "15. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:"
df_inicial = df_inicial.drop(["temp"],axis=1)


pivot_inicial = df_inicial.pivot_table(
        index=['Nombre', 'Apellido', 'Correo Electrónico', 'Curso', 'ID Asignado Por Moodle', 'Nombre De Usuario'],
        columns='Pregunta', 
        values='Respuesta', 
        aggfunc='first'
    ).reset_index()

pivot_inicial.columns = [col.replace("\n", " ").strip() for col in pivot_inicial.columns]

pivot_inicial.columns = [col.replace("\b", " ").strip() for col in pivot_inicial.columns]

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

df_avanzado = pd.read_csv('data/crudos/Avanzado.csv',
                         error_bad_lines=False, 
                         warn_bad_lines=False,
                         low_memory=False)
df_avanzado["Pregunta"] = df_avanzado["Pregunta"].str.replace("\n", " ").replace("\b", " ")
_items = df_avanzado[df_avanzado["Pregunta"] == "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia: "]["Respuesta"]
_items = _items.str.contains("TIC")
df_avanzado["temp"] = _items.copy()
df_avanzado["temp"] = df_avanzado["temp"].fillna(False)
df_avanzado.loc[df_avanzado["temp"],"Pregunta"] = "17. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:"
df_avanzado = df_avanzado.drop(["temp"],axis=1)


pivot_avanzado = df_avanzado.pivot_table(
        index=['Nombre', 'Apellido', 'Correo Electrónico', 'Curso', 'ID Asignado Por Moodle', 'Nombre De Usuario'],
        columns='Pregunta', 
        values='Respuesta', 
        aggfunc='first'
    ).reset_index()

pivot_avanzado.columns = [col.replace("\n", " ").strip() for col in pivot_avanzado.columns]

pivot_avanzado.columns = [col.replace("\b", " ").strip() for col in pivot_avanzado.columns]

##################################################################################

encuesta_caraterizacion = {
    '¿Cómo prefieres que te llamen?':
    '2. ¿Cómo prefieres que te llamen?',
    
    'Número de Cédula':
    '3. Número de Cédula',

    'Rango de edad': 
    '4. Rango de edad',

    'Mi primera lengua es español:': 
    '5. Mi primera lengua es español:',

    'Departamento de residencia': 
    '6. Departamento de residencia',

    'Municipio de residencia:': 
    '7. Municipio de residencia:',

    'Institución Educativa en la que laboro': 
    '8. Institución Educativa en la que laboro',

    '¿A qué estatuto docente pertenece?': 
    '9. ¿A qué estatuto docente pertenece?',

    'Por favor evalúa tus conocimientos de herramienta digitales del 1 al 10, según tu grado de familiarización en el manejo de los mismos (10 es muy hábil)': 
    '10. Por favor evalúa tus conocimientos de herramienta digitales del 1 al 10, según tu grado de familiarización en el manejo de los mismos (10 es muy hábil)',

    'Por favor evalúa, en la escala del 1 al 10, tus conocimientos previos sobre los contenidos pedagógicos que se estudiarán en el curso, según tu nivel de experiencia (10 es experto)': 
    '11. Por favor evalúa, en la escala del 1 al 10, tus conocimientos previos sobre los contenidos pedagógicos que se estudiarán en el curso, según tu nivel de experiencia (10 es experto)',

    'Por favor evalúa tus habilidades previas en programación, según la siguiente escala:               1. Totalmente en desacuerdo               2. En desacuerdo                    3. Neutro              4. De acuerdo                    5. Totalmente de acuerdo':
    '12. Por favor evalúa tus habilidades previas en programación, según la siguiente escala',

    'Agrega cualquier comentario adicional que quieras hacer, con relación a tus conocimientos previos y/o cómo esperas beneficiarte de los contenidos que estudiarás.': 
    "13. Agrega cualquier comentario adicional que quieras hacer, con relación a tus conocimientos previos y/o cómo espera beneficiarse de los contenidos que estudiarás.",

    'Considero que tengo la autorregulación, disciplina y responsabilidad que se requieren para ser exitoso(a) en este programa de formación virtual': 
    '14. Considero que tengo la autorregulación, disciplina y responsabilidad que se requieren para ser exitoso(a) en este programa de formación virtual',

    'Considero que los conocimientos y materiales que adquiriré durante el programa serán relevantes para mi trabajo como docente.': 
    "15. Considero que los conocimientos y materiales que adquiriré durante el programa serán relevantes para mi trabajo como docente.",

    'Considero que lo que aprenderé en el curso lo podre aplicar fácilmente en mi contexto de enseñanza/aprendizaje.': 
    "16. Considero que lo que aprenderé en el curso lo podre aplicar fácilmente en mi contexto de enseñanza/aprendizaje.",

    'Considero que los recursos de internet y equipos con los que cuento serán suficientes para participar en las actividades del curso.': 
    "17. Considero que los recursos de internet y equipos con los que cuento serán suficientes para participar en las actividades del curso.",

    'He hecho arreglos para disponer, cabalmente, del tiempo semanal requerido para desarrollar las actividades propuestas de forma adecuada.':
    "18. He hecho arreglos para disponer, cabalmente, del tiempo semanal requerido para desarrollar las actividades propuestas de forma adecuada.",

    'El o los horarios que me resultan más adecuados para asistir a los encuentros sincrónicos es/son: (Marca todas las opciones que te resulten adecuadas)': 
    "19. El o los horarios que me resultan más adecuados para asistir a los encuentros sincrónicos es/son: (Marca todas las opciones que te resulten adecuadas)"
}

pivot_inicial2 = pivot_inicial.reset_index()
pivot_avanzado2 = pivot_avanzado.reset_index()

    
aux = pivot_inicial2[encuesta_caraterizacion.keys()]  # Inicial
aux2 = pivot_avanzado2[encuesta_caraterizacion.keys()]  # Avanzado
aux = pd.concat([aux, aux2]).drop_duplicates().reset_index(drop=True)
aux.rename(encuesta_caraterizacion, axis=1, inplace=True)

# Pregunta 9
col = '10. Por favor evalúa tus conocimientos de herramienta digitales del 1 al 10, según tu grado de familiarización en el manejo de los mismos (10 es muy hábil)'
df2 = aux[col].str.split(r'\b\D+\b', expand=True)
df2.rename({
    1: '10.1 Entorno virtual de aprendizaje (Moodle)',
    2: '10.2 Herramienta para videoconferencias (Zoom)',
    3: '10.3 Almacenamiento en la nube (Google drive)',
    4: '10.4 Editor de texto (Microsoft Word o Google docs)',
    5: '10.5 Herramienta de presentación (Power Point)',
    6: '10.6 Hojas de cálculo (Microsoft Excel o Google spreadsheets)',
    7: '10.7 Herramienta de mensajería instantánea (WhatsApp)',
    8: '10.8 Correo electrónico (Gmail, Hotmail, Outlook, etc.,)',
}, axis=1, inplace=True)
df2 = df2.drop([0], axis=1)
add_columns(aux, df2)

# Pregunta 10
col = '11. Por favor evalúa, en la escala del 1 al 10, tus conocimientos previos sobre los contenidos pedagógicos que se estudiarán en el curso, según tu nivel de experiencia (10 es experto)'
df2 = aux[col].str.split(r'\b\D+\b', expand=True)
df2.rename({
    1: '11.1 Estrategias pedagógicas para promover el Pensamiento Computacional',
    2: '11.2 Gestión de Aula',
    3: '11.3 Estrategias pedagógicas para incluir más niñas en las áreas STEM',
    4: '11.4 Estrategias pedagógicas para fomentar la metacognición en los y las estudiantes',
}, axis=1, inplace=True)
df2 = df2.drop([0], axis=1)
add_columns(aux, df2)

# Pregunta 11
col = '12. Por favor evalúa tus habilidades previas en programación, según la siguiente escala'
df2 = aux[col].str.split(r'\b\D+\b', expand=True)
df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
},inplace=True)
df2.rename({
    1: '12.1 Puedo hacer un programa de computador para resolver un problema de matemáticas',
    2: '12.2 Puedo crear un programa que calcule el promedio de muchos datos en poco tiempo',
    3: '12.3 Puedo crear un programa que encienda una luz cuando una habitación esté muy oscura',
    4: '12.4 Puedo hacer un algoritmo que describa una receta de cocina',
    5: '12.5 Puedo crear un programa que pueda identificar cuando una planta necesita agua, y encienda la regadera'
}, axis=1, inplace=True)

df2 = df2.drop([0], axis=1)
add_columns(aux, df2)
if save_new:
    aux.to_excel("EncuestaCaracterización.xlsx")

