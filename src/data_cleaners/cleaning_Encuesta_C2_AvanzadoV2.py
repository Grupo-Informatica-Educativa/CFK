import pandas as pd

save_new = True

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)

otras = []

def add_columns(df1, df2):
    for col in df2.columns:
        df1[col] = df2[col]

def add_equal_columns(pivot_avanzado):
    global otras

    # Pregunta 2
    col = "2. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?"
    otras.append(col)
    opciones_preg10 = [
        "Realizar clubes y actividades extracurriculares para niñas y jóvenes como refuerzo de lo visto en las clases de áreas STEM.",
        "Destacar y reconocer los logros de las niñas y jóvenes, por ejemplo, promover concursos diferenciados por género, como, premio a la niña científica y el niño científico.",
        "Dar referencias o modelos de mujeres destacadas en las áreas STEM, por ejemplo, mostrar la película de Marie Curie.",
        "Motivar que las niñas participen y sean escuchadas, por ejemplo, alternándolas con los niños.",
        "Estimular el liderazgo femenino, por ejemplo, que las niñas y adolescentes sean representantes de grupo.",
        "Generar espacios de confianza para las niñas, por ejemplo, realizando reflexiones sobre el género al comienza de la clase",
        "Prohibir y corregir los comentarios, actitudes y acciones sexistas.",
        'Utilizar lenguaje inclusivo y no realizar estereotipos de género, por ejemplo, decir "Todas las personas" en vez de "todos los niños" o evitar decir que las niñas son delicadas.',
        "Tratos y estímulos igualitarios a toda y todo estudiante independientemente de su género.",
        "Observar el comportamiento de los niños hacia las niñas porque a ellas no se les puede tocar ni con pétalo de ua rosa."
    ]
    for count, subpregunta in enumerate(opciones_preg10):
        pivot_avanzado[f'2.{count+1} {subpregunta}'] = pivot_avanzado[col].str.contains(subpregunta).replace({
            True: "Si",
            False: "No"
        })
        otras.append(f'2.{count+1} {subpregunta}')

    # Pregunta 3
    col = "3. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia"
    df2 = pivot_avanzado[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '3.1 Es preferible que las mujeres enseñen ciencias sociales y los hombres ciencias exactas',
        2: '3.2 Es normal que la mayoría de los ingenieros mecánicos sean varones porque los hombres son mejores para los números',
        3: '3.3 Por su esencia una mujer tiene mejor desempeño en un proyecto de alto impacto social que en un proyecto de robótica industrial.',
        4: '3.4 Los hombres son mejores para la tecnología que las mujeres.',
        5: '3.5 Las mujeres tienen mayores habilidades para proyectos sociales que tecnológicos.',
        6: '3.6 Los grandes aportes en la computación han sido hechos por hombres.',
        7: '3.7 Que la mayoría de mujeres no opte por áreas exactas es simplemente cuestión de preferencias.',
        8: '3.8 Que la mayoría de personas en artes y humanidades sean mujeres es muestra de su sensibilidad.', 
        9: '3.9 Es natural que los hombres sea buenos para los números y las mujeres para las letras',
        10: '3.10 Los hombres son muy ágiles tomando decisiones importantes.',
        11: '3.11 Las niñas son más ordenadas que los niños.',
        12: '3.12 Muchas mujeres se caracterizan por una pureza que pocos hombres poseen',
        13: '3.13 Las mujeres deben ser queridas y protegidas por los hombres',
        14: '3.14 Todo hombre debe tener una mujer a quien amar',
        15: '3.15 El hombre está incompleto sin la mujer',
        16: '3.16 Las mujeres en comparación con los hombres tienden a tener un sentido más refinado de la cultura y el buen gusto',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_avanzado, df2)
    otras.append(col)
    otras.extend(df2.columns)

    # Pregunta 5
    col = "5. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:"
    df2 = pivot_avanzado[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '5.1 Sé cómo resolver los problemas técnicos cuando fallan las TIC',
        2: '5.2 Puedo aprender sobre nuevas tecnologías fácilmente',
        3: '5.3 Sé cómo usar las TIC con los estudiantes en clase',
        4: '5.4 Me apoyo en mis colegas para resolver problemas sobre cómo trabajar algún tema',
        5: '5.5 Puedo hablar con otros docentes sobre el diseño de cursos',
        6: '5.6 Siento que tengo apoyo de otros docentes para el diseño de mis cursos',
        7: '5.7 No tengo con quién conversar sobre el diseño de mis cursos',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_avanzado, df2)
    otras.append(col)
    otras.extend(df2.columns)

    # Pregunta 7
    col = "7. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional"
    df2 = pivot_avanzado[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '7.1 Usar el correo electrónico',
        2: '7.2 Crear y usar de modelos y simulaciones',
        3: '7.3 Automatizar tareas',
        4: '7.4 Usar Word',
        5: '7.5 Procesar Datos',
        6: '7.6 Resolver problemas a través de herramientas computacionales (como simulaciones)',
        7: '7.7 Resolver problemas a través de herramientas computacionales (como lenguajes de programación)',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_avanzado, df2)
    otras.append(col)
    otras.extend(df2.columns)

    # Pregunta 8
    col = "8. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos"
    df2 = pivot_avanzado[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '8.1 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi trabajo',
        2: '8.2 Puedo definir el pensamiento computacional',
        3: '8.3 Puedo describir las prácticas y habilidades que componen el pensamiento computacional a mis estudiantes',
        4: '8.4 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi vida diaria',
        5: '8.5 Creo que tengo las habilidades para desarrollar el pensamiento computacional en mis estudiantes',
        6: '8.6 Puedo enseñar fácilmente sobre nuevas prácticas computacionales',
        7: '8.7 Puedo diseñar una clase que desarrolle el pensamiento computacional en los estudiantes',
        8: '8.8 Puedo seleccionar tecnologías para usar en mi salón de clases, que me permitan mejorar qué enseño y cómo enseño pensamiento computacional',
        9: '8.9 Puedo aplicar mis habilidades en pensamiento computacional para ayudar a los estudiantes a perseguir sus intereses individuales',
        10: '8.10 Puedo implementar y evaluar la idoneidad de una estrategia pedagógica que le permita a los estudiantes desarrollar pensamiento computacional'
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_avanzado, df2)
    otras.append(col)
    otras.extend(df2.columns)
    
    # Pregunta 10
    col = "10. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional"
    pivot_avanzado[col] = pivot_avanzado[col].str.replace('-1', '0')
    df2 = pivot_avanzado[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '10.1 Actividades desconectadas',
        2: '10.2 Usa-Modifica-Crea',
        3: '10.3 Clase magistral',
        4: '10.4 Enseñanza explícita y sin ambigüedades',
        5: '10.5 Marcha Silenciosa',
        6: '10.6 Aprendizaje basado en proyectos',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_avanzado, df2)
    otras.append(col)
    otras.extend(df2.columns)

    # Pregunta 12
    col = "12. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:"
    pivot_avanzado[col] = pivot_avanzado[col].str.replace('-1', '0')
    df2 = pivot_avanzado[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '12.1 Le explicaría la respuesta correcta',
        2: '12.2 Le sugeriría ir paso a paso por el programa simulando su ejecución',
        3: '12.3 Le diría que revise sus notas',
        4: '12.4 Le sugeriría que revise las memorias colectivas',
        5: '12.5 Le sugeriría volver a leer el problema',
        6: '12.6 Le sugeriría intentar con varios valores para evaluar el programa',
        7: '12.7 Le explicaría el problema nuevamente',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_avanzado, df2)
    otras.append(col)
    otras.extend(df2.columns)

#########################

df_avanzado = pd.read_csv('data/crudos/Avanzado.csv',
                         error_bad_lines=False, 
                         warn_bad_lines=False,
                         low_memory=False)
df_avanzado["Pregunta"] = df_avanzado["Pregunta"].str.replace("\n", " ").replace("\b", " ")
_items = df_avanzado[df_avanzado["Pregunta"] == "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia: "]["Respuesta"]
_items = _items.str.contains("TIC")
df_avanzado["temp"] = _items.copy()
df_avanzado["temp"] = df_avanzado["temp"].fillna(False)
df_avanzado.loc[df_avanzado["temp"],"Pregunta"] = "5. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:"
df_avanzado = df_avanzado.drop(["temp"],axis=1)


pivot_avanzado = df_avanzado.pivot_table(
        index=['Nombre', 'Apellido', 'Correo Electrónico', 'Curso', 'ID Asignado Por Moodle', 'Nombre De Usuario'],
        columns='Pregunta', 
        values='Respuesta', 
        aggfunc='first'
    ).reset_index()

pivot_avanzado.columns = [col.replace("\n", " ").strip() for col in pivot_avanzado.columns]

pivot_avanzado.columns = [col.replace("\b", " ").strip() for col in pivot_avanzado.columns]


#########################

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

    'Por favor evalúa tus habilidades previas en programación, según la siguiente escala':
    '12. Por favor evalúa tus habilidades previas en programación, según la siguiente escala',

    'Agrega cualquier comentario adicional que quieras hacer, con relación a tus conocimientos previos y/o cómo esperas beneficiarte de los contenidos que estudiarás.': 
    "3. Agrega cualquier comentario adicional que quieras hacer, con relación a tus conocimientos previos y/o cómo espera beneficiarse de los contenidos que estudiarás.",

    'Considero que tengo la autorregulación, disciplina y responsabilidad que se requieren para ser exitoso(a) en este programa de formación virtual': 
    '14. Considero que tengo la autorregulación, disciplina y responsabilidad que se requieren para ser exitoso(a) en este programa de formación virtual',

    'Considero que los conocimientos y materiales que adquiriré durante el programa serán relevantes para mi trabajo como docente.': 
    "3. Considero que los conocimientos y materiales que adquiriré durante el programa serán relevantes para mi trabajo como docente.",

    'Considero que lo que aprenderé en el curso lo podre aplicar fácilmente en mi contexto de enseñanza/aprendizaje.': 
    "16. Considero que lo que aprenderé en el curso lo podre aplicar fácilmente en mi contexto de enseñanza/aprendizaje.",

    'Considero que los recursos de internet y equipos con los que cuento serán suficientes para participar en las actividades del curso.': 
    "5. Considero que los recursos de internet y equipos con los que cuento serán suficientes para participar en las actividades del curso.",

    'He hecho arreglos para disponer, cabalmente, del tiempo semanal requerido para desarrollar las actividades propuestas de forma adecuada.':
    "18. He hecho arreglos para disponer, cabalmente, del tiempo semanal requerido para desarrollar las actividades propuestas de forma adecuada.",

    'El o los horarios que me resultan más adecuados para asistir a los encuentros sincrónicos es/son: (Marca todas las opciones que te resulten adecuadas)': 
    "7. El o los horarios que me resultan más adecuados para asistir a los encuentros sincrónicos es/son: (Marca todas las opciones que te resulten adecuadas)"
}

for a in pivot_avanzado.columns:
    if "Por favor evalúa tus habilidades previas en programación" in a:
        aux = a

pivot_avanzado2 = pivot_avanzado.rename(columns={aux:'Por favor evalúa tus habilidades previas en programación, según la siguiente escala'}) 
to_drop = list(encuesta_caraterizacion.keys())

#########################

preguntas_info_inicial = {
    "Nombre De Usuario": 
    "1. Cédula",

    "Cuáles de las siguientes estrategias usted ha usado en sus clases?": 
    "2. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?",
   
    "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:": 
    "3. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia",

    "5. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:":
    "5. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:",

   
    "Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional:": 
    "7. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional",

    "Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos:": 
    "8. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos",

    "En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional.": 
    "10. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional",

    "Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:": 
    "12. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:",
}

preguntas_propias_rename = {
    "La contaminación en las principales ciudades del país es algo que preocupa a los gobernantes. La contaminación atmosférica del aire se miden con un valor llamado el Índice de Calidad del Aire (ICA).   La siguiente tabla muestra los valores para los cuales el ICA representa una calidad del aire Buena, Regular, Mala, y Muy Mala.    Como el programa que creó Nicolás mostró que el aire en el centro de la ciudad estaba muy contaminado en ciertos momentos, Por lo tanto, el alcalde decidió tomar medidas extremas. Revise el siguiente programa y elija la opción que describe la medida que     tomó el alcalde.": 
    "14. La contaminación en las principales ciudades del país es algo que preocupa a los gobernantes. Las concentraciones de contaminantes se miden con un valor llamado el Índice de Calidad del Aire (ICA).   La siguiente tabla muestra los valores para los cuales el ICA representa una calidad del aire Buena, Regular, Mala, y Muy Mala.Como el programa que creó Nicolás mostró que el aire en el centro de la ciudad estaba muy contaminado en ciertos momentos, el alcalde decidió tomar medidas extremas. Revisa el siguiente programa y elije la opción que describe la medida que tomó el alcalde.",

    "Dada la definición de la función:¿Cuál de las siguientes afirmaciones describe mejor el llamado a la función sumar (8, 5, 12)?": 
    "15. Dada la definición de la función:¿Cuál de las siguientes afirmaciones describe mejor el llamado a la función sumar (8, 5, 12)?",

    "Considera el siguiente segmento de código:Seleccione el fragmento de código más correcto que resultará en el cálculo del área de la superficie de un cilindro, dada la fórmula:a) b) c) d) e)": 
    "16. Considera el siguiente segmento de código:Seleccione el fragmento de código más correcto que resultará en el cálculo del área de la superficie de un cilindro, dada la fórmula:",

    "Considera el siguiente segmento de código:¿En qué orden deberá realizar las siguientes operaciones de manera que el valor de la variable “a” sea 15 al finalizar?": 
    "17. Considera el siguiente segmento de código:¿En qué orden deberá realizar las siguientes operaciones de manera que el valor de la variable “a” sea 15 al finalizar?",

    "Tim examina cada una de las siguientes piezas de código y responde que la primera termina con X siendo igual a 5, y la segunda con X siendo igual a 16.¿Cuál es el error conceptual de Tim?": 
    "18. Tim examina cada una de las siguientes piezas de código y responde que la primera termina con X siendo igual a 5, y la segunda con X siendo igual a 16.¿Cuál es el error conceptual de Tim?",

    "María vive cerca de una montaña donde hace mucho calor en el día, pero mucho frío en la noche. Ella tiene calefacción y aire acondicionado en su apartamento, pero deben prenderlo desde la portería que está en el primer piso del edificio. María decidió     programar la Micro:bit para que envíe un mensaje de encender la calefacción cuando esté frío (menos de 15 grados) y encender el aire acondicionado cuando esté caliente (más de 25 grados).   ¿Cuál de los siguientes programas le podríafuncionar a María?                            Imagen 1                                                              Imagen 2                                                                        Imagen 3                                                             Imagen 4":
    "19. María vive cerca de una montaña donde hace mucho calor en el día, pero mucho frío en la noche. Ella tiene calefacción y aire acondicionado en su apartamento, pero deben prenderlo desde la portería que está en el primer piso del edificio. María decidió     programar la Micro:bit para que envíe un mensaje de encender la calefacción cuando esté frío (menos de 3 grados) y encender el aire acondicionado cuando esté caliente (más de 25 grados).   ¿Cuál de los siguientes programas le podríafuncionar a María?",
    
    "Juan y Andrea crearon un juego en la Micro:bit y lo compartieron con sus compañeros. Sin embargo, nadie parece entender de qué se trata. ¿De qué crees que trata el juego?": 
    "20. Juan y Andrea crearon un juego en la Micro:bit y lo compartieron con sus compañeros. Sin embargo, nadie parece entender de qué se trata.",

    "¿Cómo le ayudarías a Juan y Andrea a explicarle a sus compañeros de clase el juego que han diseñado?": 
    "21. ¿Cómo le ayudarías a Juan y Andrea a explicarle a sus compañeros de clase el juego que han diseñado?",

    "La alcaldía contrató a Valeria para realizar un programa en la micro:bit que controle el alumbrado público de su ciudad. Al utilizar el sensor de luz de la tarjeta micro:bit, detectó que cuando mide los niveles de luz con un valor por debajo de 100, está lo suficientemente oscuro como para encender las luces del alumbrado público. El programa que hizo funciona bien para encender el alumbrado de la ciudad pero, cuando amanece, las luces quedan encendidas durante todo el día.  Valeria no está segura de cómo solucionarlo, aunque tiene algunas ideas que podrían funcionar. ¿Cuál de las siguientes opciones cree que debería usar Valeria?                            Imagen 1                                            Imagen 2                                                      Imagen 3                                            Imagen 4":
    "22. La alcaldía contrató a Valeria para realizar un programa en la micro:bit que controle el alumbrado público de su ciudad. Al utilizar el sensor de luz de la tarjeta micro:bit, detectó que cuando mide los niveles de luz con un valor por debajo de 100, está lo suficientemente oscuro como para encender las luces del alumbrado público. El programa que hizo funciona bien para encender el alumbrado de la ciudad pero, cuando amanece, las luces quedan encendidas durante todo el día.  Valeria no está segura de cómo solucionarlo, aunque tiene algunas ideas que podrían funcionar. ¿Cuál de las siguientes opciones cree que debería usar Valeria?",

    "Dada la siguiente función y llamado:         ¿Cuál de las siguientes afirmaciones es verdadera?":
    "23. Dada la siguiente función y llamado: ¿Cuál de las siguientes afirmaciones es verdadera?"
}   

#########################

col_inicial = [i for i in pivot_avanzado2.columns if i.startswith(
    'Por favor evalúa tus habilidades previas en programación')][0]

pivot_avanzado3 = pivot_avanzado2.reset_index()
pivot_avanzado3 = pivot_avanzado2.drop(to_drop, axis=1)


merged = preguntas_info_inicial | preguntas_propias_rename
cols =[]
for e in merged:
    cols.append(merged[e])


pivot_avanzado.rename(merged, axis=1, inplace=True)
add_equal_columns(pivot_avanzado)
merge = []
merge.extend(otras)
merge.extend(cols)
for a in merge:
    if a not in pivot_avanzado:
        print(a)
        print("#"*8)


pivot_avanzado[merge].to_excel("PostestAvanzado.xlsx", encoding='utf-8-sig')
