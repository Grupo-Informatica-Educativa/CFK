import pandas as pd

save_new = True

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)


def add_columns(df1, df2):
    for col in df2.columns:
        df1[col] = df2[col]

df_inicial = pd.read_csv('data/crudos/Encuesta_Inicio_29521.csv',
                         error_bad_lines=False, warn_bad_lines=False,
                         low_memory=False)
df_avanzado = pd.read_csv('data/crudos/Encuesta_Avanzado_29521.csv',
                          error_bad_lines=False, warn_bad_lines=False,
                          low_memory=False)
#

pivot_inicial = df_inicial.pivot_table(index=['Nombre', 'Apellido', 'Correo Electrónico', 'Curso', 'ID Asignado Por Moodle', 'Nombre De Usuario'],
                                       columns='Pregunta', values='Respuesta', aggfunc='first').reset_index()

pivot_avanzado = df_avanzado.pivot_table(index=['Nombre', 'Apellido', 'Correo Electrónico', 'Curso', 'ID Asignado Por Moodle', 'Nombre De Usuario'],
                                         columns='Pregunta', values='Respuesta', aggfunc='first').reset_index()

'''
preg30 = ''
for col in pivot_avanzado.columns:
    if("La alcaldía acaba de contratar a Valeria para hacer un programa en la Micro:bit que controle el alumbrado público de su ciudad" in col):
        print(pivot_avanzado[col].count())
        if (pivot_avanzado[col].count() > 100):
            preg30 = col
'''

# Preguntas compartidas // Las que son iguales en ambas tabla
preguntas_compartidas = {
    "ID Asignado Por Moodle": "ID Moodle",
    "Nombre De Usuario": "Cédula",
    "Nombre": "Nombre",
    "Apellido": "Apellido",
    "Correo Electrónico": "Correo Electrónico",
    "Curso": "Curso",
    "Edad (años)": "Edad",
    "Su institución está en un contexto:": "Contexto IE",
    "Género:": "Género",
    "¿Hace parte de alguno de los siguientes grupos étnicos?": "Grupo Étnico",
    "¿Cuál es su estrato socioeconómico?": "Estrato",
    '¿Es usted cabeza de hogar?': '¿Es usted cabeza de hogar? ',
    '¿Es usted líder comunitario?': '¿Es usted líder comunitario?',
    "¿Cuáles de las siguientes áreas enseña y en qué grado? (Marque 'NS/NC' si no enseña el área)": "9. ¿Cuáles de las siguientes áreas enseña y en qué grado? (Marque 'NS/NC' si no enseña el área)",
    "¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Selección múltiple con múltiple respuesta)": "10. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Selección múltiple con múltiple respuesta)",
    "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo):": "11. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)",
    "Agrega cualquier comentario o clarificación sobre las preguntas anteriores.": "12 .Comentario o clarificación sobre las preguntas anteriores",
    "Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)": "13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)",
    "Agrega cualquier comentario o clarificación sobre las preguntas anteriores.": "14. Comentario o clarificación sobre las preguntas anteriores",
    "Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional (izquierda totalmente des acuerdo y derecha totalmente de acuerdo):": "15. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)",
    "Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos (izquierda totalmente des acuerdo y derecha totalmente de acuerdo):": "16. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)",
    "En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional.": "18. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional",
    "Agrega cualquier comentario o clarificación adicional sobre las estrategias de enseñanza de la pregunta anterior.": "19. Comentario o clarificación adicional sobre las estrategias de enseñanza de la pregunta anterior",
    "Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:": "20. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:",
}

encuesta_caraterizacion = {
    'Número de Cédula': '2. Número de Cédula',
    '¿Cómo prefieres que te llamen?': '3. ¿Cómo prefieres que te llamen?',
    'Rango de edad': '4. Rango de edad',
    'Mi primera lengua es español:': '5. Mi primera lengua es español:',
    'Departamento de residencia': '6. Departamento de residencia',
    'Municipio de residencia:': '7. Municipio de residencia:',
    'Institución Educativa en la que laboro': '8. Institución Educativa en la que laboro',
    'Por favor evalúa tus conocimientos de herramienta digitales del 1 al 10, según tu grado de familiarización en el manejo de los mismos (10 es muy hábil)': '9. Por favor evalúa tus conocimientos de herramienta digitales del 1 al 10, según tu grado de familiarización en el manejo de los mismos (10 es muy hábil)',
    'Por favor evalúa, en la escala del 1 al 10, tus conocimientos previos sobre los contenidos pedagógicos que se estudiarán en el curso, según tu nivel de experiencia (10 es experto)': '10. Por favor evalúa, en la escala del 1 al 10, tus conocimientos previos sobre los contenidos pedagógicos que se estudiarán en el curso, según tu nivel de experiencia (10 es experto)',
    'Por favor evalúa tus habilidades previas en programación, según la siguiente escala:               1. Totalmente en desacuerdo               2. En desacuerdo                    3. Neutro              4. De acuerdo                    5. Totalmente de acuerdo': '11. Por favor evalúa tus habilidades previas en programación, según la siguiente escala',
    'Agrega cualquier comentario adicional que quieras hacer, con relación a tus conocimientos previos y/o cómo espera beneficiarse de los contenidos que estudiará.': "12. Agrega cualquier comentario adicional que quieras hacer, con relación a tus conocimientos previos y/o cómo espera beneficiarse de los contenidos que estudiará.",
    'Considero que tengo la autorregulación, disciplina y responsabilidad que se requieren para ser exitoso(a) en este programa de formación virtual': '13. Considero que tengo la autorregulación, disciplina y responsabilidad que se requieren para ser exitoso(a) en este programa de formación virtual',
    'Considero que los conocimientos y materiales que adquiriré durante el programa serán relevantes para mi trabajo como docente.': "14. Considero que los conocimientos y materiales que adquiriré durante el programa serán relevantes para mi trabajo como docente.",
    'Considero que lo que aprenderé en el curso lo podre aplicar fácilmente en mi contexto de enseñanza/aprendizaje.': "15. Considero que lo que aprenderé en el curso lo podre aplicar fácilmente en mi contexto de enseñanza/aprendizaje.",
    'Considero que los recursos de internet y equipos con los que cuento serán suficientes para participar en las actividades del curso.': "16. Considero que los recursos de internet y equipos con los que cuento serán suficientes para participar en las actividades del curso.",
    'He hecho arreglos para disponer, cabalmente, del tiempo semanal requerido para desarrollar las actividades propuestas de forma adecuada.': "17. He hecho arreglos para disponer, cabalmente, del tiempo semanal requerido para desarrollar las actividades propuestas de forma adecuada.",
    'El o los horarios que me resultan más adecuados para asistir a los encuentros sincrónicos es/son: (Marca todas las opciones que te resulten adecuadas)': "18. El o los horarios que me resultan más adecuados para asistir a los encuentros sincrónicos es/son: (Marca todas las opciones que te resulten adecuadas)"
}

pretest_inicial = [
    "ID Moodle",
    "Cédula",
    "Nombre",
    "Apellido",
    "Correo Electrónico",
    "Curso",
    "Edad",
    "Contexto IE",
    "Género",
    "Grupo Étnico",
    "Estrato",
    '¿Es usted cabeza de hogar? ',
    '¿Es usted líder comunitario?',
    "22. La docente Margarita decidió hacer que sus estudiantes de segundo de primaria utilicen los computadores del colegio para predecir el clima de una semana (temperatura, precipitaciones, y viento). Cada estudiante debe dibujar cómo se verá el clima en la ciudad en dicha semana. Margarita, creó un archivo compartido donde los estudiantes ingresarán la información. Luego tomaron las predicciones de modelos de Internet y los ingresaron en el mismo documento compartido. Durante una semana tomaron los datos reales, y luego, proyectaron en el tablero los datos predichos por los estudiantes, los del modelo de Internet, y los datos reales. Al finalizar, Margarita les mostró a los estudiantes cómo hacer un gráfico para comparar los diferentes datos. ¿Está Margarita desarrollando el pensamiento computacional de sus estudiantes? Seleccione todas las respuestas que considere correctas.",
    "23. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo. Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando encuentra una que comienza con Trujillo, mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí. ¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.",
    "24. Un ratón robot ha sido programado para seguir instrucciones. ¿En cuál de los tubos debería comenzar el robot para llegar al queso?",
    "25. Andrea hizo un diagrama de flujo para diseñar el algoritmo que le permitirá encender automáticamente el ventilador cuando esté muy caliente su habitación. Sin embargo, no está segura de que funcione. ¿Qué le podrías recomendar?",
    "26. Considera el siguiente segmento de código ¿Después de que el anterior código se ejecuta, cual es el valor de la variable secuela?",
    "27. Considera el siguiente código: Si a=3, b=8 y c=10, ¿Qué imprimirá el programa?",
    "28. Considera el siguiente código: Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados son verdaderos?",
    "29. Suponiendo que “a” y “b” son variables booleanas. Considera la siguiente expresión lógica:¿Cuál de las siguientes afirmaciones describe de manera más precisa la evaluación de las expresiones?",
    "31. Teniendo en cuenta el siguiente fragmento de código, Alejandra responde a la pregunta ¿Cuál será el valor final de “Y”? afirmando que el valor final será 44. El código retorna 120 ¿Qué opinas de la respuesta de Alejandra?",
    "33. ¿Cómo le ayudarías a comprender la diferencia entre los dos códigos?",
]

pretest_avanzado = [
    "ID Moodle",
    "Cédula",
    "Nombre",
    "Apellido",
    "Correo Electrónico",
    "Curso",
    "Edad",
    "Contexto IE",
    "Género",
    "Grupo Étnico",
    "Estrato",
    '¿Es usted cabeza de hogar? ',
    '¿Es usted líder comunitario?',
    "22. La contaminación en las principales ciudades del país es algo que preocupa a los gobernantes. Las concentraciones de contaminantes se miden con un valor llamado el Índice de Calidad del Aire (ICA).   La siguiente tabla muestra los valores para los cuales el ICA representa una calidad del aire Buena, Regular, Mala, y Muy Mala.Como el programa que creó Nicolás mostró que el aire en el centro de la ciudad estaba muy contaminado en ciertos momentos, el alcalde decidió tomar medidas extremas. Revisa el siguiente programa y elije la opción que describe la medida que tomó el alcalde.",
    "23. Dada la definición de la función:¿Cuál de las siguientes afirmaciones describe mejor el llamado a la función sumar (8, 5, 12)?",
    "24. Considera el siguiente segmento de código:Seleccione el fragmento de código más correcto que resultará en el cálculo del área de la superficie de un cilindro, dada la fórmula:",
    "25. Considera el siguiente segmento de código:¿En qué orden deberá realizar las siguientes operaciones de manera que el valor de la variable “a” sea 15 al finalizar?",
    "26. Tim examina cada una de las siguientes piezas de código y responde que la primera termina con X siendo igual a 5, y la segunda con X siendo igual a 16.¿Cuál es el error conceptual de Tim?",
    "27. María vive cerca de una montaña donde hace mucho calor en el día, pero mucho frío en la noche. Ella tiene calefacción y aire acondicionado en su apartamento, pero deben prenderlo desde la portería que está en el primer piso del edificio. María decidió     programar la Micro:bit para que envíe un mensaje de encender la calefacción cuando esté frío (menos de 15 grados) y encender el aire acondicionado cuando esté caliente (más de 25 grados).   ¿Cuál de los siguientes programas le podríafuncionar a María?                            Imagen 1                                                              Imagen 2                                                                        Imagen 3                                                             Imagen 4",
    "28. Juan y Andrea crearon un juego en la Micro:bit y lo compartieron con sus compañeros. Sin embargo, nadie parece entender de qué se trata.",
    "29. ¿Cómo le ayudarías a Juan y Andrea a explicarle a sus compañeros de clase el juego que han diseñado?",
]

pretest_iguales = [
    "9. ¿Cuáles de las siguientes áreas enseña y en qué grado? (Marque 'NS/NC' si no enseña el área)",
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
    "10. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Selección múltiple con múltiple respuesta)",
    "10.1 Promover actividades que no perpetúen estereotipos de género, por ejemplo, que las niñas y adolescentes jueguen a la construcción y ensamble.",
    "10.2 Realizar clubes y actividades extracurriculares para niñas y jóvenes como refuerzo de lo visto en las clases de áreas STEM.",
    "10.3 Destacar y reconocer los logros de las niñas y jóvenes, por ejemplo, promover concursos diferenciados por género, como, premio a la niña científica y el niño científico.",
    "10.4 Dedicar una clase exclusiva a reflexionar sobre el género, por ejemplo, con una película, una lectura o una conversación, etc",
    "10.5 Dar referencias o modelos de mujeres destacadas en las áreas STEM, por ejemplo, mostrar la película de Marie Curie.",
    "11. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)",
    '11.1 Es preferible que las mujeres enseñen ciencias sociales y los hombres ciencias exactas',
    '11.2 Es necesario que haya igual número de mujeres ganadoras del nobel de física como hombres',
    '11.3 Es normal que la mayoría de los ingenieros mecánicos sean varones porque los hombres son mejores para los números',
    '11.4 Las becas en áreas STEM que son sólo para mujeres discriminan a los hombres y generan desigualdad',
    '11.5 Que haya más físicos que físicas se explica por una historia de dominación masculina',
    '11.6 Muchas mujeres se caracterizan por una pureza que pocos hombres poseen',
    '11.7 Las mujeres deben ser queridas y protegidas por los hombres',
    '11.8 Todo hombre debe tener una mujer a quien amar',
    '11.9 El hombre está incompleto sin la mujer',
    '11.10 Las mujeres en comparación con los hombres tienden a tener un sentido más refinado de la cultura y el buen gusto',
    '11.11 Los hombres deberían estar dispuestos a sacrificar su propio bienestar con el fin de proveer seguridad económica a las mujeres',
    "13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)",
    '13.1 Sé cómo resolver los problemas técnicos cuando fallan las TIC',
    '13.2 Puedo aprender sobre nuevas tecnologías fácilmente',
    '13.3 Sé cómo usar las TIC con los estudiantes en clase',
    '13.4 Me apoyo en mis colegas para resolver problemas sobre cómo trabajar algún tema',
    '13.5 Puedo hablar con otros docentes sobre el diseño de cursos',
    '13.6 Siento que tengo apoyo de otros docentes para el diseño de mis cursos',
    '13.7 No tengo con quién conversar sobre el diseño de mis cursos',
    "15. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)",
    '15.1 Usar el correo electrónico',
    '15.2 Crear y usar de modelos y simulaciones',
    '15.3 Automatizar tareas',
    '15.4 Usar Word',
    '15.5 Procesar Datos',
    '15.6 Resolver problemas a través de herramientas computacionales (como simulaciones)',
    '15.7 Resolver problemas a través de herramientas computacionales (como lenguajes de programación)',
    "16. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)",
    '16.1 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi trabajo',
    '16.2 Puedo definir el pensamiento computacional',
    '16.3 Puedo describir las prácticas y habilidades que componen el pensamiento computacional a mis estudiantes',
    '16.4 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi vida diaria',
    '16.5 Creo que tengo las habilidades para desarrollar el pensamiento computacional en mis estudiantes',
    '16.6 Puedo enseñar fácilmente sobre nuevas prácticas computacionales',
    '16.7 Puedo diseñar una clase que desarrolle el pensamiento computacional en los estudiantes',
    '16.8 Puedo seleccionar tecnologías para usar en mi salón de clases, que me permitan mejorar qué enseño y cómo enseño pensamiento computacional',
    '16.9 Puedo aplicar mis habilidades en pensamiento computacional para ayudar a los estudiantes a perseguir sus intereses individuales',
    '16.10 Puedo implementar y evaluar la idoneidad de una estrategia pedagógica que le permita a los estudiantes desarrollar pensamiento computacional ',
    "18. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional",
    '18.1 Actividades desconectadas',
    '18.2 Usa-Modifica-Crea',
    '18.3 Clase magistral',
    '18.4 Enseñanza explícita y sin ambigüedades',
    '18.5 Marcha Silenciosa',
    '18.6 Aprendizaje basado en proyectos',
    "20. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:",
    '20.1 Le explicaría la respuesta correcta',
    '20.2 Le sugeriría ir paso a paso por el programa simulando su ejecución ',
    '20.3 Le diría que revise sus notas',
    '20.4 Le sugeriría que revise las memorias colectivas',
    '20.5 Le sugeriría volver a leer el problema',
    '20.6 Le sugeriría intentar con varios valores para evaluar el programa',
    '20.7 Le explicaría el problema nuevamente',
]

to_drop = list(encuesta_caraterizacion.keys())

pivot_inicial.columns = [col.replace("\n", " ").strip()
                         for col in pivot_inicial.columns]
pivot_avanzado.columns = [col.replace(
    "\n", " ").strip() for col in pivot_avanzado.columns]


def fix_caracterizacion(df, df2):
    # Hacer merge de las dos bases de datos
    aux = df[to_drop]  # Inicial
    aux2 = df2[to_drop]  # Avanzado
    aux = pd.concat([aux, aux2]).drop_duplicates().reset_index(drop=True)
    aux.rename(encuesta_caraterizacion, axis=1, inplace=True)

    # Pregunta 9
    col = '9. Por favor evalúa tus conocimientos de herramienta digitales del 1 al 10, según tu grado de familiarización en el manejo de los mismos (10 es muy hábil)'
    df2 = aux[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '9.1 Entorno virtual de aprendizaje (Moodle)',
        2: '9.2 Herramienta para videoconferencias (Zoom)',
        3: '9.3 Almacenamiento en la nube (Google drive)',
        4: '9.4 Editor de texto (Microsoft Word o Google docs)',
        5: '9.5 Herramienta de presentación (Power Point)',
        6: '9.6 Hojas de cálculo (Microsoft Excel o Google spreadsheets)',
        7: '9.7 Herramienta de mensajería instantánea (WhatsApp)',
        8: '9.8 Correo electrónico (Gmail, Hotmail, Outlook, etc.,)',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(aux, df2)

    # Pregunta 10
    col = '10. Por favor evalúa, en la escala del 1 al 10, tus conocimientos previos sobre los contenidos pedagógicos que se estudiarán en el curso, según tu nivel de experiencia (10 es experto)'
    df2 = aux[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '10.1 Estrategias pedagógicas para promover el Pensamiento Computacional',
        2: '10.2 Gestión de Aula',
        3: '10.3 Estrategias pedagógicas para incluir más niñas en las áreas STEM',
        4: '10.4 Estrategias pedagógicas para fomentar la metacognición en los y las estudiantes',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(aux, df2)

    # Pregunta 11
    col = '11. Por favor evalúa tus habilidades previas en programación, según la siguiente escala'
    df2 = aux[col].str.split(r'\b\D+\b', expand=True)

    df2.rename({
        1: '11.1 Puedo hacer un programa de computador para resolver un problema de matemáticas',
        2: '11.2 Puedo crear un programa que calcule el promedio de muchos datos en poco tiempo',
        3: '11.3 Puedo crear un programa que encienda una luz cuando una habitación esté muy oscura',
        4: '11.4 Puedo hacer un algoritmo que describa una receta de cocina',
        5: '11.5 Puedo crear un programa que pueda identificar cuando una planta necesita agua, y encienda la regadera'
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(aux, df2)
    if save_new:
        aux.to_excel("EncuestaCaracterización.xlsx")


col_inicial = [i for i in pivot_inicial.columns if i.startswith(
    'Por favor evalúa tus habilidades previas en programación')][0]
col_avanzado = [i for i in pivot_avanzado.columns if i.startswith(
    'Por favor evalúa tus habilidades previas en programación')][0]

pivot_inicial.rename({col_inicial: col_avanzado}, axis=1, inplace=True)
col_inicial = [i for i in pivot_inicial.columns if i.startswith(
    'Por favor evalúa tus habilidades previas en programación')][0]

fix_caracterizacion(pivot_inicial, pivot_avanzado)


pivot_inicial = pivot_inicial.reset_index()
pivot_inicial = pivot_inicial.drop(to_drop, axis=1)
pivot_inicial.rename(preguntas_compartidas, axis=1, inplace=True)
pivot_avanzado = pivot_avanzado.reset_index()
pivot_avanzado = pivot_avanzado.drop(to_drop, axis=1)
pivot_avanzado.rename(preguntas_compartidas, axis=1, inplace=True)

# Limpiamos las preguntas en común y las volvemos columnas
# Pregunta 9
# Pregunta 10
# Pregunta 11
# Pregunta 13
# Pregunta 15
# Pregunta 16
# Pregunta 18
# Pregunta 20
def add_equal_columns(pivot_inicial):
    # Pregunta 9
    col = "9. ¿Cuáles de las siguientes áreas enseña y en qué grado? (Marque 'NS/NC' si no enseña el área)"
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
    # Pregunta 10
    col = "10. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Selección múltiple con múltiple respuesta)"
    opciones_preg10 = [
        "Promover actividades que no perpetúen estereotipos de género, por ejemplo, que las niñas y adolescentes jueguen a la construcción y ensamble.",
        "Realizar clubes y actividades extracurriculares para niñas y jóvenes como refuerzo de lo visto en las clases de áreas STEM.",
        "Destacar y reconocer los logros de las niñas y jóvenes, por ejemplo, promover concursos diferenciados por género, como, premio a la niña científica y el niño científico.",
        "Dedicar una clase exclusiva a reflexionar sobre el género, por ejemplo, con una película, una lectura o una conversación, etc",
        "Dar referencias o modelos de mujeres destacadas en las áreas STEM, por ejemplo, mostrar la película de Marie Curie."
    ]
    for count, subpregunta in enumerate(opciones_preg10):
        pivot_inicial[f'10.{count+1} {subpregunta}'] = pivot_inicial[col].str.contains(
            subpregunta)

    # Pregunta 11
    col = "11. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '11.1 Es preferible que las mujeres enseñen ciencias sociales y los hombres ciencias exactas',
        2: '11.2 Es necesario que haya igual número de mujeres ganadoras del nobel de física como hombres',
        3: '11.3 Es normal que la mayoría de los ingenieros mecánicos sean varones porque los hombres son mejores para los números',
        4: '11.4 Las becas en áreas STEM que son sólo para mujeres discriminan a los hombres y generan desigualdad',
        5: '11.5 Que haya más físicos que físicas se explica por una historia de dominación masculina',
        6: '11.6 Muchas mujeres se caracterizan por una pureza que pocos hombres poseen',
        7: '11.7 Las mujeres deben ser queridas y protegidas por los hombres',
        8: '11.8 Todo hombre debe tener una mujer a quien amar',
        9: '11.9 El hombre está incompleto sin la mujer',
        10: '11.10 Las mujeres en comparación con los hombres tienden a tener un sentido más refinado de la cultura y el buen gusto',
        11: '11.11 Los hombres deberían estar dispuestos a sacrificar su propio bienestar con el fin de proveer seguridad económica a las mujeres'
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 13
    col = "13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '13.1 Sé cómo resolver los problemas técnicos cuando fallan las TIC',
        2: '13.2 Puedo aprender sobre nuevas tecnologías fácilmente',
        3: '13.3 Sé cómo usar las TIC con los estudiantes en clase',
        4: '13.4 Me apoyo en mis colegas para resolver problemas sobre cómo trabajar algún tema',
        5: '13.5 Puedo hablar con otros docentes sobre el diseño de cursos',
        6: '13.6 Siento que tengo apoyo de otros docentes para el diseño de mis cursos',
        7: '13.7 No tengo con quién conversar sobre el diseño de mis cursos',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 15
    col = "15. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '15.1 Usar el correo electrónico',
        2: '15.2 Crear y usar de modelos y simulaciones',
        3: '15.3 Automatizar tareas',
        4: '15.4 Usar Word',
        5: '15.5 Procesar Datos',
        6: '15.6 Resolver problemas a través de herramientas computacionales (como simulaciones)',
        7: '15.7 Resolver problemas a través de herramientas computacionales (como lenguajes de programación)',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 16
    col = "16. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)"
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '16.1 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi trabajo',
        2: '16.2 Puedo definir el pensamiento computacional',
        3: '16.3 Puedo describir las prácticas y habilidades que componen el pensamiento computacional a mis estudiantes',
        4: '16.4 Puedo aplicar las prácticas y habilidades del pensamiento computacional a mi vida diaria',
        5: '16.5 Creo que tengo las habilidades para desarrollar el pensamiento computacional en mis estudiantes',
        6: '16.6 Puedo enseñar fácilmente sobre nuevas prácticas computacionales',
        7: '16.7 Puedo diseñar una clase que desarrolle el pensamiento computacional en los estudiantes',
        8: '16.8 Puedo seleccionar tecnologías para usar en mi salón de clases, que me permitan mejorar qué enseño y cómo enseño pensamiento computacional',
        9: '16.9 Puedo aplicar mis habilidades en pensamiento computacional para ayudar a los estudiantes a perseguir sus intereses individuales',
        10: '16.10 Puedo implementar y evaluar la idoneidad de una estrategia pedagógica que le permita a los estudiantes desarrollar pensamiento computacional '
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 18
    col = "18. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional"
    pivot_inicial[col] = pivot_inicial[col].str.replace('-1', '0')
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '18.1 Actividades desconectadas',
        2: '18.2 Usa-Modifica-Crea',
        3: '18.3 Clase magistral',
        4: '18.4 Enseñanza explícita y sin ambigüedades',
        5: '18.5 Marcha Silenciosa',
        6: '18.6 Aprendizaje basado en proyectos',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)
    # Pregunta 20
    col = "20. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:"
    pivot_inicial[col] = pivot_inicial[col].str.replace('-1', '0')
    df2 = pivot_inicial[col].str.split(r'\b\D+\b', expand=True)
    df2.rename({
        1: '20.1 Le explicaría la respuesta correcta',
        2: '20.2 Le sugeriría ir paso a paso por el programa simulando su ejecución ',
        3: '20.3 Le diría que revise sus notas',
        4: '20.4 Le sugeriría que revise las memorias colectivas',
        5: '20.5 Le sugeriría volver a leer el problema',
        6: '20.6 Le sugeriría intentar con varios valores para evaluar el programa',
        7: '20.7 Le explicaría el problema nuevamente',
    }, axis=1, inplace=True)
    df2 = df2.drop([0], axis=1)
    add_columns(pivot_inicial, df2)


def fix_avanzado(df):
    preguntas_rename = {
        "La contaminación en las principales ciudades del país es algo que preocupa a los gobernantes. Las concentraciones de contaminantes se miden con un valor llamado el Índice de Calidad del Aire (ICA).   La siguiente tabla muestra los valores para los cuales el ICA representa una calidad del aire Buena, Regular, Mala, y Muy Mala.Como el programa que creó Nicolás mostró que el aire en el centro de la ciudad estaba muy contaminado en ciertos momentos, el alcalde decidió tomar medidas extremas. Revisa el siguiente programa y elije la opción que describe la medida que tomó el alcalde.": "22. La contaminación en las principales ciudades del país es algo que preocupa a los gobernantes. Las concentraciones de contaminantes se miden con un valor llamado el Índice de Calidad del Aire (ICA).   La siguiente tabla muestra los valores para los cuales el ICA representa una calidad del aire Buena, Regular, Mala, y Muy Mala.Como el programa que creó Nicolás mostró que el aire en el centro de la ciudad estaba muy contaminado en ciertos momentos, el alcalde decidió tomar medidas extremas. Revisa el siguiente programa y elije la opción que describe la medida que tomó el alcalde.",
        "Dada la definición de la función:¿Cuál de las siguientes afirmaciones describe mejor el llamado a la función sumar (8, 5, 12)?": "23. Dada la definición de la función:¿Cuál de las siguientes afirmaciones describe mejor el llamado a la función sumar (8, 5, 12)?",
        "Considera el siguiente segmento de código:Seleccione el fragmento de código más correcto que resultará en el cálculo del área de la superficie de un cilindro, dada la fórmula:": "24. Considera el siguiente segmento de código:Seleccione el fragmento de código más correcto que resultará en el cálculo del área de la superficie de un cilindro, dada la fórmula:",
        "Considera el siguiente segmento de código:¿En qué orden deberá realizar las siguientes operaciones de manera que el valor de la variable “a” sea 15 al finalizar?": "25. Considera el siguiente segmento de código:¿En qué orden deberá realizar las siguientes operaciones de manera que el valor de la variable “a” sea 15 al finalizar?",
        "Tim examina cada una de las siguientes piezas de código y responde que la primera termina con X siendo igual a 5, y la segunda con X siendo igual a 16.¿Cuál es el error conceptual de Tim?": "26. Tim examina cada una de las siguientes piezas de código y responde que la primera termina con X siendo igual a 5, y la segunda con X siendo igual a 16.¿Cuál es el error conceptual de Tim?",
        "Juan y Andrea crearon un juego en la Micro:bit y lo compartieron con sus compañeros. Sin embargo, nadie parece entender de qué se trata.": "28. Juan y Andrea crearon un juego en la Micro:bit y lo compartieron con sus compañeros. Sin embargo, nadie parece entender de qué se trata.",
        "¿Cómo le ayudarías a Juan y Andrea a explicarle a sus compañeros de clase el juego que han diseñado?": "29. ¿Cómo le ayudarías a Juan y Andrea a explicarle a sus compañeros de clase el juego que han diseñado?",
    }
    df.rename(preguntas_rename, axis=1, inplace=True)


def fix_inicial(df):
    preguntas_rename = {
        "La docente Margarita decidió hacer que sus estudiantes de segundo de primaria utilicen los computadores del colegio para predecir el clima de una semana (temperatura, precipitaciones, y viento). Cada estudiante debe dibujar cómo se verá el clima en la ciudad en dicha semana. Margarita, creó un archivo compartido donde los estudiantes ingresarán la información. Luego tomaron las predicciones de modelos de Internet y los ingresaron en el mismo documento compartido. Durante una semana tomaron los datos reales, y luego, proyectaron en el tablero los datos predichos por los estudiantes, los del modelo de Internet, y los datos reales. Al finalizar, Margarita les mostró a los estudiantes cómo hacer un gráfico para comparar los diferentes datos.    ¿Está Margarita desarrollando el pensamiento computacional de sus estudiantes? Seleccione todas las respuestas que considere correctas.": "22. La docente Margarita decidió hacer que sus estudiantes de segundo de primaria utilicen los computadores del colegio para predecir el clima de una semana (temperatura, precipitaciones, y viento). Cada estudiante debe dibujar cómo se verá el clima en la ciudad en dicha semana. Margarita, creó un archivo compartido donde los estudiantes ingresarán la información. Luego tomaron las predicciones de modelos de Internet y los ingresaron en el mismo documento compartido. Durante una semana tomaron los datos reales, y luego, proyectaron en el tablero los datos predichos por los estudiantes, los del modelo de Internet, y los datos reales. Al finalizar, Margarita les mostró a los estudiantes cómo hacer un gráfico para comparar los diferentes datos. ¿Está Margarita desarrollando el pensamiento computacional de sus estudiantes? Seleccione todas las respuestas que considere correctas.",
        "La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo. Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando encuentra una que comienza con Trujillo, mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí.  ¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.": "23. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo. Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando encuentra una que comienza con Trujillo, mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí. ¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.",
        "Un ratón robot ha sido programado para seguir las siguientes instrucciones:  (1) Sigue hacia abajo hasta que haya un cruce a uno de los lados (2) Cuando encuentres un cruce, atraviésalo (3) Vuelve al paso (1).  Considera el siguiente laberinto para nuestro ratón robot. ¿En cuál de los tubos debería comenzar el robot para llegar al queso?": "24. Un ratón robot ha sido programado para seguir instrucciones. ¿En cuál de los tubos debería comenzar el robot para llegar al queso?",
        "Andrea hizo un diagrama de flujo para diseñar el algoritmo que le permitirá encender automáticamente el ventilador cuando esté muy caliente su habitación. Sin embargo, no está segura de que funcione. ¿Qué le podrías recomendar?": "25. Andrea hizo un diagrama de flujo para diseñar el algoritmo que le permitirá encender automáticamente el ventilador cuando esté muy caliente su habitación. Sin embargo, no está segura de que funcione. ¿Qué le podrías recomendar?",
        "Considera el siguiente segmento de código¿Después de que el anterior código se ejecuta, cual es el valor de la variable secuela?": "26. Considera el siguiente segmento de código ¿Después de que el anterior código se ejecuta, cual es el valor de la variable secuela?",
        "Considera el siguiente código: Si a=3, b=8 y c=10, ¿Qué imprimirá el programa?": "27. Considera el siguiente código: Si a=3, b=8 y c=10, ¿Qué imprimirá el programa?",
        "Considera el siguiente código: Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados sonverdaderos?": "28. Considera el siguiente código: Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados son verdaderos?",
        "Suponiendo que “a” y “b” son variables booleanas. Considera la siguiente expresión lógica:¿Cuál de las siguientes afirmaciones describe de manera más precisa la evaluación de las expresiones?": "29. Suponiendo que “a” y “b” son variables booleanas. Considera la siguiente expresión lógica:¿Cuál de las siguientes afirmaciones describe de manera más precisa la evaluación de las expresiones?",
        "Teniendo en cuenta el siguiente fragmento de código, Alejandra responde a la pregunta ¿Cuál será el valor final de “Y”? afirmando que el valor final será 44. El código retorna 120¿Qué opinas de la respuesta de Alejandra?": "31. Teniendo en cuenta el siguiente fragmento de código, Alejandra responde a la pregunta ¿Cuál será el valor final de “Y”? afirmando que el valor final será 44. El código retorna 120 ¿Qué opinas de la respuesta de Alejandra?",
        "¿Cómo le ayudarías a comprender la diferencia entre los dos códigos?": "33. ¿Cómo le ayudarías a comprender la diferencia entre los dos códigos?",
    }
    df.rename(preguntas_rename, axis=1, inplace=True)


add_equal_columns(pivot_inicial)
add_equal_columns(pivot_avanzado)
fix_inicial(pivot_inicial)
fix_avanzado(pivot_avanzado)


if save_new:
    merge = pretest_inicial + pretest_iguales
    pivot_inicial[merge].to_excel("PretestInicial.xlsx", encoding='utf-8-sig')
    merge2 = pretest_avanzado + pretest_iguales
    pivot_avanzado[merge2].to_excel("PretestAvanzado.xlsx", encoding='utf-8-sig')
