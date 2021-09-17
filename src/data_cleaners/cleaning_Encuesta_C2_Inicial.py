import pandas as pd

save_new = True

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)



def add_columns(df1, df2):
    for col in df2.columns:
        df1[col] = df2[col]

def add_equal_columns(pivot_inicial):
    # Pregunta 9
    col = "9. ¿Cuáles de las siguientes áreas enseña y en qué grado?"
    pivot_inicial[col] = pivot_inicial[col].str.replace('-1', '0')
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '9.1 Ciencias naturales y educación ambiental',
        2: '9.2 Ciencias sociales, historia, geografía, constitución política y democracia',
        3: '9.3 Educación artística',
        4: '9.4 Educación ética y en valores humanos',
        5: '9.5 Educación física, recreación y deportes',
        6: '9.6 Educación religiosa',
        7: '9.7 Humanidades, lengua castellana e idiomas extranjeros',
        8: '9.8 Matemáticas',
        9: '9.9 Tecnología e informática',
        10: '9.10 Otro',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)

    # Pregunta 12
    col = "12. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?"
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
        pivot_inicial[f'12.{count+1} {subpregunta}'] = pivot_inicial[col].str.contains(subpregunta).replace({
            True: "Si",
            False: "No"
        })

    # Pregunta 13
    col = "13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '13.1 Es preferible que las mujeres enseñen ciencias sociales y los hombres ciencias exactas',
        2: '13.2 Es normal que la mayoría de los ingenieros mecánicos sean varones porque los hombres son mejores para los números',
        3: '13.3 Por su esencia una mujer tiene mejor desempeño en un proyecto de alto impacto social que en un proyecto de robótica industrial.',
        4: '13.4 Los hombres son mejores para la tecnología que las mujeres.',
        5: '13.5 Las mujeres tienen mayores habilidades para proyectos sociales que tecnológicos.',
        6: '13.6 Los grandes aportes en la computación han sido hechos por hombres.',
        7: '13.7 Que la mayoría de mujeres no opte por áreas exactas es simplemente cuestión de preferencias.',
        8: '13.8 Que la mayoría de personas en artes y humanidades sean mujeres es muestra de su sensibilidad.', 
        9: '13.9 Es natural que los hombres sea buenos para los números y las mujeres para las letras',
        10: '13.10 Los hombres son muy ágiles tomando decisiones importantes.',
        11: '13.11 Las niñas son más ordenadas que los niños.',
        12: '13.12 Muchas mujeres se caracterizan por una pureza que pocos hombres poseen',
        13: '13.13 Las mujeres deben ser queridas y protegidas por los hombres',
        14: '13.14 Todo hombre debe tener una mujer a quien amar',
        15: '13.15 El hombre está incompleto sin la mujer',
        16: '13.16 Las mujeres en comparación con los hombres tienden a tener un sentido más refinado de la cultura y el buen gusto',
    }, axis=1, inplace=True)
    
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 15
    col = "15. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '15.1 Sé cómo resolver los problemas técnicos cuando fallan las TIC',
        2: '15.2 Puedo aprender sobre nuevas tecnologías fácilmente',
        3: '15.3 Sé cómo usar las TIC con los estudiantes en clase',
        4: '15.4 Me apoyo en mis colegas para resolver problemas sobre cómo trabajar algún tema',
        5: '15.5 Puedo hablar con otros docentes sobre el diseño de cursos',
        6: '15.6 Siento que tengo apoyo de otros docentes para el diseño de mis cursos',
        7: '15.7 No tengo con quién conversar sobre el diseño de mis cursos',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 17
    col = "17. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '17.1 Usar el correo electrónico',
        2: '17.2 Crear y usar de modelos y simulaciones',
        3: '17.3 Automatizar tareas',
        4: '17.4 Usar Word',
        5: '17.5 Procesar Datos',
        6: '17.6 Resolver problemas a través de herramientas computacionales (como simulaciones)',
        7: '17.7 Resolver problemas a través de herramientas computacionales (como lenguajes de programación)',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)

    # Pregunta 18
    col = "18. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.replace({
        "1": "Totalmente en desacuerdo",
        "2": "En desacuerdo",
        "3": "Neutro",
        "4": "De acuerdo",
        "5": "Totalmente de acuerdo",
    },inplace=True)
    df2.rename({
        1: '18.1 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi trabajo',
        2: '18.2 Puedo definir el pensamiento computacional',
        3: '18.3 Puedo describir las prácticas y habilidades que componen el pensamiento computacional a mis estudiantes',
        4: '18.4 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi vida diaria',
        5: '18.5 Creo que tengo las habilidades para desarrollar el pensamiento computacional en mis estudiantes',
        6: '18.6 Puedo enseñar fácilmente sobre nuevas prácticas computacionales',
        7: '18.7 Puedo diseñar una clase que desarrolle el pensamiento computacional en los estudiantes',
        8: '18.8 Puedo seleccionar tecnologías para usar en mi salón de clases, que me permitan mejorar qué enseño y cómo enseño pensamiento computacional',
        9: '18.9 Puedo aplicar mis habilidades en pensamiento computacional para ayudar a los estudiantes a perseguir sus intereses individuales',
        10: '18.10 Puedo implementar y evaluar la idoneidad de una estrategia pedagógica que le permita a los estudiantes desarrollar pensamiento computacional'
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 20
    col = "20. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional"
    pivot_inicial[col] = pivot_inicial[col].str.replace('-1', '0')
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '20.1 Actividades desconectadas',
        2: '20.2 Usa-Modifica-Crea',
        3: '20.3 Clase magistral',
        4: '20.4 Enseñanza explícita y sin ambigüedades',
        5: '20.5 Marcha Silenciosa',
        6: '20.6 Aprendizaje basado en proyectos',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 22
    col = "22. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:"
    pivot_inicial[col] = pivot_inicial[col].str.replace('-1', '0')
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '22.1 Le explicaría la respuesta correcta',
        2: '22.2 Le sugeriría ir paso a paso por el programa simulando su ejecución',
        3: '22.3 Le diría que revise sus notas',
        4: '22.4 Le sugeriría que revise las memorias colectivas',
        5: '22.5 Le sugeriría volver a leer el problema',
        6: '22.6 Le sugeriría intentar con varios valores para evaluar el programa',
        7: '22.7 Le explicaría el problema nuevamente',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)

otras = [
    "9. ¿Cuáles de las siguientes áreas enseña y en qué grado?",
    '9.1 Ciencias naturales y educación ambiental',
    '9.2 Ciencias sociales, historia, geografía, constitución política y democracia',
    '9.3 Educación artística',
    '9.4 Educación ética y en valores humanos',
    '9.5 Educación física, recreación y deportes',
    '9.6 Educación religiosa',
    '9.7 Humanidades, lengua castellana e idiomas extranjeros',
    '9.8 Matemáticas',
    '9.9 Tecnología e informática',
    '9.10 Otro',
    "12. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?",
    "12.1 Realizar clubes y actividades extracurriculares para niñas y jóvenes como refuerzo de lo visto en las clases de áreas STEM.",
    "12.2 Destacar y reconocer los logros de las niñas y jóvenes, por ejemplo, promover concursos diferenciados por género, como, premio a la niña científica y el niño científico.",
    "12.3 Dar referencias o modelos de mujeres destacadas en las áreas STEM, por ejemplo, mostrar la película de Marie Curie.",
    "12.4 Motivar que las niñas participen y sean escuchadas, por ejemplo, alternándolas con los niños.",
    "12.5 Estimular el liderazgo femenino, por ejemplo, que las niñas y adolescentes sean representantes de grupo.",
    "12.6 Generar espacios de confianza para las niñas, por ejemplo, realizando reflexiones sobre el género al comienza de la clase",
    "12.7 Prohibir y corregir los comentarios, actitudes y acciones sexistas.",
    '12.8 Utilizar lenguaje inclusivo y no realizar estereotipos de género, por ejemplo, decir "Todas las personas" en vez de "todos los niños" o evitar decir que las niñas son delicadas.',
    "12.9 Tratos y estímulos igualitarios a toda y todo estudiante independientemente de su género.",
    "12.10 Observar el comportamiento de los niños hacia las niñas porque a ellas no se les puede tocar ni con pétalo de ua rosa.",
    "13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia",
    '13.1 Es preferible que las mujeres enseñen ciencias sociales y los hombres ciencias exactas',
    '13.2 Es normal que la mayoría de los ingenieros mecánicos sean varones porque los hombres son mejores para los números',
    '13.3 Por su esencia una mujer tiene mejor desempeño en un proyecto de alto impacto social que en un proyecto de robótica industrial.',
    '13.4 Los hombres son mejores para la tecnología que las mujeres.',
    '13.5 Las mujeres tienen mayores habilidades para proyectos sociales que tecnológicos.',
    '13.6 Los grandes aportes en la computación han sido hechos por hombres.',
    '13.7 Que la mayoría de mujeres no opte por áreas exactas es simplemente cuestión de preferencias.',
    '13.8 Que la mayoría de personas en artes y humanidades sean mujeres es muestra de su sensibilidad.', 
    '13.9 Es natural que los hombres sea buenos para los números y las mujeres para las letras',
    '13.10 Los hombres son muy ágiles tomando decisiones importantes.',
    '13.11 Las niñas son más ordenadas que los niños.',
    '13.12 Muchas mujeres se caracterizan por una pureza que pocos hombres poseen',
    '13.13 Las mujeres deben ser queridas y protegidas por los hombres',
    '13.14 Todo hombre debe tener una mujer a quien amar',
    '13.15 El hombre está incompleto sin la mujer',
    '13.16 Las mujeres en comparación con los hombres tienden a tener un sentido más refinado de la cultura y el buen gusto',
    '15.1 Sé cómo resolver los problemas técnicos cuando fallan las TIC',
    '15.2 Puedo aprender sobre nuevas tecnologías fácilmente',
    '15.3 Sé cómo usar las TIC con los estudiantes en clase',
    '15.4 Me apoyo en mis colegas para resolver problemas sobre cómo trabajar algún tema',
    '15.5 Puedo hablar con otros docentes sobre el diseño de cursos',
    '15.6 Siento que tengo apoyo de otros docentes para el diseño de mis cursos',
    '15.7 No tengo con quién conversar sobre el diseño de mis cursos',
    "17. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional",
    '17.1 Usar el correo electrónico',
    '17.2 Crear y usar de modelos y simulaciones',
    '17.3 Automatizar tareas',
    '17.4 Usar Word',
    '17.5 Procesar Datos',
    '17.6 Resolver problemas a través de herramientas computacionales (como simulaciones)',
    '17.7 Resolver problemas a través de herramientas computacionales (como lenguajes de programación)',
    "18. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos",
    '18.1 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi trabajo',
    '18.2 Puedo definir el pensamiento computacional',
    '18.3 Puedo describir las prácticas y habilidades que componen el pensamiento computacional a mis estudiantes',
    '18.4 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi vida diaria',
    '18.5 Creo que tengo las habilidades para desarrollar el pensamiento computacional en mis estudiantes',
    '18.6 Puedo enseñar fácilmente sobre nuevas prácticas computacionales',
    '18.7 Puedo diseñar una clase que desarrolle el pensamiento computacional en los estudiantes',
    '18.8 Puedo seleccionar tecnologías para usar en mi salón de clases, que me permitan mejorar qué enseño y cómo enseño pensamiento computacional',
    '18.9 Puedo aplicar mis habilidades en pensamiento computacional para ayudar a los estudiantes a perseguir sus intereses individuales',
    '18.10 Puedo implementar y evaluar la idoneidad de una estrategia pedagógica que le permita a los estudiantes desarrollar pensamiento computacional',
    "20. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional",
    '20.1 Actividades desconectadas',
    '20.2 Usa-Modifica-Crea',
    '20.3 Clase magistral',
    '20.4 Enseñanza explícita y sin ambigüedades',
    '20.5 Marcha Silenciosa',
    '20.6 Aprendizaje basado en proyectos',
    "22. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:",
    '22.1 Le explicaría la respuesta correcta',
    '22.2 Le sugeriría ir paso a paso por el programa simulando su ejecución',
    '22.3 Le diría que revise sus notas',
    '22.4 Le sugeriría que revise las memorias colectivas',
    '22.5 Le sugeriría volver a leer el problema',
    '22.6 Le sugeriría intentar con varios valores para evaluar el programa',
    '22.7 Le explicaría el problema nuevamente'
        
]

#########################

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

df_inicial.columns = [col.replace("\n", " ").strip() for col in df_inicial.columns]



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

for a in pivot_inicial.columns:
    if "Por favor evalúa tus habilidades previas en programación" in a:
        aux = a

pivot_inicial2 = pivot_inicial.rename(columns={aux:'Por favor evalúa tus habilidades previas en programación, según la siguiente escala'}) 
to_drop = list(encuesta_caraterizacion.keys())

for col in pivot_inicial.columns:
    if "verdaderos" in col:
        aux = a

pivot_inicial2 = pivot_inicial2.rename(columns={aux:'30. Considera el siguiente código: Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados son verdaderos?'}) 

#########################

preguntas_info_inicial = {
    "ID Asignado Por Moodle": "ID Moodle",
    "Nombre": "Nombre",
    "Apellido": "Apellido",
    "Correo Electrónico": "Correo Electrónico",
    "Curso": "Curso",

    "Nombre De Usuario": 
    "1. Cédula",

    "Edad (Años)": 
    "2. Edad",

    "Su institución está en un contexto:": 
    "3. Contexto IE",

    "Género:": 
    "4. Género",

    '¿Es usted cabeza de hogar?': 
    '5. ¿Es usted cabeza de hogar? ',

    '¿Cuál es su estado civil?':
    '6. ¿Cuál es su estado civil?',

    'Número de horas de clases semanales que orienta (Solo números)': 
    '7. Número de horas de clases semanales que orienta',

    '¿Es usted líder comunitario?':
    '8. ¿Es usted líder comunitario?',

    "¿Cuáles de las siguientes áreas enseña y en qué grado? (Marque 'NS/NC' si no enseña el área)": 
    "9. ¿Cuáles de las siguientes áreas enseña y en qué grado?",

    '¿De acuerdo con lo anterior, usted es docente de áreas STEM (ciencias naturales, matemática, tecnología e informática) o No STEM (ciencias sociales, educación artística, educación física, educación religiosa, humanidades e idiomas extranjeros)?':
    '10. ¿De acuerdo con lo anterior, usted es docente de áreas STEM o No STEM?',

    'Su formación es en áreas' : 
    '11. Su formación es en áreas',

    "¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Opción múltiple)": 
    "12. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?",
    
    "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:": 
    "13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia",

    "Agregue cualquier comentario o aclaración sobre las preguntas anteriores.": 
    "14 .Comentario o clarificación sobre las preguntas anteriores",

    "15. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:":
    "15. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:",

    #"Agrega cualquier comentario o clarificación sobre las preguntas anteriores.": 
    #"16. Comentario o clarificación sobre las preguntas anteriores",

    "Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional:": 
    "17. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional",

    "Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos:": 
    "18. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos",

    #"Agrega cualquier comentario o clarificación sobre las preguntas anteriores.": 
    #"19 .Comentario o clarificación sobre las preguntas anteriores",

    "En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional. Si no conoce alguna práctica pedagógica, por favor elija la opción NS/NC.": 
    "20. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional",

    #"Agrega cualquier comentario o clarificación adicional sobre las estrategias de enseñanza de la pregunta anterior.": 
    #"21. Comentario o clarificación adicional sobre las estrategias de enseñanza de la pregunta anterior",
    
    "Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:": 
    "22. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:",
}

preguntas_propias_rename = {
    "La docente Margarita decidió hacer que sus estudiantes de segundo de primaria utilicen los computadores del colegio para predecir el clima de una semana (temperatura, precipitaciones, y viento). Cada estudiante debe dibujar cómo se verá el clima en la     ciudad en dicha semana. Margarita, creó un archivo compartido donde los estudiantes ingresarán la información. Luego tomaron las predicciones de modelos de Internet y los ingresaron en el mismo documento compartido. Durante una semana tomaron los     datos reales, y luego, proyectaron en el tablero los datos predichos por los estudiantes, los del modelo de Internet, y los datos reales. Al finalizar, Margarita les mostró a los estudiantes cómo hacer un gráfico para comparar los diferentes datos.    ¿Está Margarita desarrollando el pensamiento computacional de sus estudiantes? Seleccione todas las respuestas que considere correctas.":
    "24. La docente Margarita decidió hacer que sus estudiantes de segundo de primaria utilicen los computadores del colegio para predecir el clima de una semana (temperatura, precipitaciones, y viento). Cada estudiante debe dibujar cómo se verá el clima en la ciudad en dicha semana. Margarita, creó un archivo compartido donde los estudiantes ingresarán la información. Luego tomaron las predicciones de modelos de Internet y los ingresaron en el mismo documento compartido. Durante una semana tomaron los datos reales, y luego, proyectaron en el tablero los datos predichos por los estudiantes, los del modelo de Internet, y los datos reales. Al finalizar, Margarita les mostró a los estudiantes cómo hacer un gráfico para comparar los diferentes datos. ¿Está Margarita desarrollando el pensamiento computacional de sus estudiantes? Seleccione todas las respuestas que considere correctas.",

    "La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo. Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando encuentra una que comienza con Trujillo, mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí.  ¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.": 
    "25. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo. Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando encuentra una que comienza con Trujillo, mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí. ¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.",

    "Un ratón robot ha sido programado para seguir las siguientes instrucciones:  (1) Sigue hacia abajo hasta que haya un cruce a uno de los lados (2) Cuando encuentres un cruce, atraviésalo (3) Vuelve al paso (1).  Considera el siguiente laberinto para nuestro ratón robot. ¿En cuál de los tubos debería comenzar el robot para llegar al queso?": 
    "26. Un ratón robot ha sido programado para seguir instrucciones. ¿En cuál de los tubos debería comenzar el robot para llegar al queso?",

    "Andrea hizo un diagrama de flujo para diseñar el algoritmo que le permitirá encender automáticamente el ventilador cuando esté muy caliente su habitación. Sin embargo, no está segura de que funcione. ¿Qué le podrías recomendar?":
    "27. Andrea hizo un diagrama de flujo para diseñar el algoritmo que le permitirá encender automáticamente el ventilador cuando esté muy caliente su habitación. Sin embargo, no está segura de que funcione. ¿Qué le podrías recomendar?",

    "Considera el siguiente segmento de código¿Después de que el anterior código se ejecuta, cual es el valor de la variable secuela?":
    "28. Considera el siguiente segmento de código ¿Después de que el anterior código se ejecuta, cual es el valor de la variable secuela?",

    "Considera el siguiente código: Si a=3, b=8 y c=10, ¿Qué imprimirá el programa?": 
    "29. Considera el siguiente código: Si a=3, b=8 y c=10, ¿Qué imprimirá el programa?",

    #" código: Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados sonverdaderos? ": 
    #"30. Considera el siguiente código: Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados son verdaderos?",

    "Suponiendo que “a” y “b” son variables booleanas. Considera la siguiente expresión lógica:¿Cuál de las siguientes afirmaciones describe de manera más precisa la evaluación de las expresiones?": 
    "31. Suponiendo que “a” y “b” son variables booleanas. Considera la siguiente expresión lógica:¿Cuál de las siguientes afirmaciones describe de manera más precisa la evaluación de las expresiones?",

    "La alcaldía acaba de contratar a Valeria para hacer un programa en la Micro:bit que controle el alumbrado público de su ciudad. Utilizando el sensor de luz de la tarjeta Micro:bit, ella se dio cuenta que cuando mide niveles de luz con un valor por debajo     de 100, ya está suficientemente oscuro como para prender el alumbrado público. El programa que hizo funciona bien para prender el alumbrado de la ciudad, pero luego cuando amanece, las luces siguen encendidas durante todo el día.   Valeria no está segura cómo solucionarlo, pero tiene algunas ideas que cree que podrían funcionar. ¿Cuál de las siguientes opciones crees que debería usar Valeria?                 Imagen 1                 Imagen 2                       Imagen 3                 Imagen 4":
    "32. La alcaldía acaba de contratar a Valeria para hacer un programa en la Micro:bit que controle el alumbrado público de su ciudad. Utilizando el sensor de luz de la tarjeta Micro:bit, ella se dio cuenta que cuando mide niveles de luz con un valor por debajo     de 100, ya está suficientemente oscuro como para prender el alumbrado público. El programa que hizo funciona bien para prender el alumbrado de la ciudad, pero luego cuando amanece, las luces siguen encendidas durante todo el día.   Valeria no está segura cómo solucionarlo, pero tiene algunas ideas que cree que podrían funcionar. ¿Cuál de las siguientes opciones crees que debería usar Valeria?",

    "¿Qué botella debe cambiarse de color para que el resultado final sea una botella de color blanco? Tenga en cuenta lo que hace cada máquina recicladora que se usa en este sistema.":
    "33. ¿Qué botella debe cambiarse de color para que el resultado final sea una botella de color blanco? Tenga en cuenta lo que hace cada máquina recicladora que se usa en este sistema.",

    "Teniendo en cuenta el siguiente fragmento de código, Alejandra responde a la pregunta ¿Cuál será el valor final de “Y”? afirmando que el valor final será 44. El código retorna 120¿Qué opinas de la respuesta de Alejandra?": 
    "34. Teniendo en cuenta el siguiente fragmento de código, Alejandra responde a la pregunta ¿Cuál será el valor final de “Y”? afirmando que el valor final será 44. El código retorna 120 ¿Qué opinas de la respuesta de Alejandra?",
}

#########################

col_inicial = [i for i in pivot_inicial2.columns if i.startswith(
    'Por favor evalúa tus habilidades previas en programación')][0]

pivot_inicial3 = pivot_inicial2.reset_index()
pivot_inicial3 = pivot_inicial2.drop(to_drop, axis=1)


merged = preguntas_info_inicial | preguntas_propias_rename
cols =[]
for e in merged:
    cols.append(merged[e])


pivot_inicial.rename(merged, axis=1, inplace=True)
add_equal_columns(pivot_inicial)
merge = []
merge.extend(otras)
merge.extend(cols)
pivot_inicial[merge].to_excel("PretestInicial.xlsx", encoding='utf-8-sig')
