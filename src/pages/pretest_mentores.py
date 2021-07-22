import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *
from src.utils.answers_funcs import *

files = [
    {
        "title": "Autoeficacia",
        "file":  "pre_mentores_autoeficacia.xlsx",
    },
    {
        "title": "Conocimientos",
        "file":  "pre_mentores_conocimientos.xlsx",
        "respuestas": {
            '22. La contaminación en las principales ciudades del país es algo que preocupa a los gobernantes. Las concentraciones de contaminantes se miden con un valor llamado el Índice de Calidad del Aire (ICA).  La siguiente tabla muestra los valores para los cuales el ICA representa una calidad del aire Buena, Regular, Mala, y Muy Mala.Como el programa que creó Nicolás mostró que el aire en el centro de la ciudad estaba muy contaminado en ciertos momentos, el alcalde decidió tomar medidas extremas. Revisa el siguiente programa y elije la opción que describe la medida que tomó el alcalde.': 'Cerrar el centro para carros mientras la calidad del aire sea mala, muy mala, o extremadamente mala.',
            '27. María vive cerca de una montaña donde hace mucho calor en el día, pero mucho frío en la noche. Ella tiene calefacción y aire acondicionado en su apartamento, pero deben prenderlo desde la portería que está en el primer piso del edificio. María decidió     programar la Micro:bit para que envíe un mensaje de encender la calefacción cuando esté frío (menos de 15 grados) y encender el aire acondicionado cuando esté caliente (más de 25 grados).  ¿Cuál de los siguientes programas le podríafuncionar a María?                Imagen 1                 Imagen 2                   Imagen 3                 Imagen 4': 'Imagen 3',
            'Andrea hizo un diagrama de flujo para diseñar el algoritmo que le permitirá encender automáticamente el ventilador cuando esté muy caliente su habitación. Sin embargo, no está segura de que funcione. ¿Qué le podrías recomendar?': 'El programa no funciona, debe capturar nuevamente el valor de la temperatura luego de encender el ventilador',
            'Considera el siguiente código:Después de que se ejecute el código anterior, ¿Cuáles de los siguientes enunciados sonverdaderos?': 'II y III',
            'Considera el siguiente código:Sia=3, b=8 y c=10, ¿Qué imprimirá el programa?': '10',
            'Considera el siguiente segmento de código:Seleccione el fragmento de código más correcto que resultará en el cálculo del área de la superficie de un cilindro, dada la fórmula:': 'x ::2 * 3.14 * r  →  y ::x * r  → z ::h * x  → areaSuperficie :: y + z',
            'Considera el siguiente segmento de código:¿En qué orden deberá realizar las siguientes operaciones de manera que el valor de la variable “a” sea 15 al finalizar?': 'alfa, delta, gama, beta, épsilon',
            'Considera el siguiente segmento de código¿Después de que el anterior código se ejecuta, cual es el valor de la variable secuela?': '6',
            'Dada la definición de la función:¿Cuál de las siguientes afirmaciones describe mejor el llamado a la función sumar (8, 5, 12)?': 'Esta función no imprime nunca nada',
            'Juan y Andrea crearon un juego en la Micro:bit y lo compartieron con sus compañeros. Sin embargo, nadie parece entender de qué se trata.': 'Cada uno tiene un número asignado y gana solamente si presiona su botón cuando sale este número',
            'La alcaldía acaba de contratar a Valeria para hacer un programa en la Micro:bit que controle el alumbrado público de su ciudad. Utilizando el sensor de luz de la tarjeta Micro:bit, ella se dio cuenta que cuando mide niveles de luz con un valor por debajo     de 100, ya está suficientemente oscuro como para prender el alumbrado público. El programa que hizo funciona bien para prender el alumbrado de la ciudad, pero luego cuando amanece, las luces siguen encendidas durante todo el día.   Valeria no está segura cómo solucionarlo, pero tiene algunas ideas que cree que podrían funcionar. ¿Cuál de las siguientes opciones crees que debería usar Valeria?                 Imagen 1                  Imagen 2                    Imagen 3                  Imagen 4': 'Imagen 3',
            'Suponiendo que “a” y “b” son variables booleanas. Considera la siguiente expresión lógica:¿Cuál de las siguientes afirmaciones describe de manera más precisa la evaluación de las expresiones?': 'La segunda expresión es verdadera si “(a O b)” es verdadero',
            'Teniendo en cuenta el siguiente fragmento de código, Alejandra responde a la pregunta ¿Cuál será el valor final de “Y”? afirmando que el valor final será 44. El código retorna 120   ¿Qué opinas de la respuesta de Alejandra?': 'Está equivocada, el resultado es 120.',
            'Tim examina cada una de las siguientes piezas de código y responde que la primera termina con X siendo igual a 5, y la segunda con X siendo igual a 16.¿Cuál es el error conceptual de Tim?': 'Cree que, si la condición se cumple, todo lo que sigue se va a ejecutar',
            'Un ratón robot ha sido programado para seguir las siguientes instrucciones:(1)Sigue hacia abajo hasta que haya un cruce a uno de los lados(2) Cuando encuentres un cruce, atraviésalo(3) Vuelve al paso (1).Considera el siguiente laberinto para nuestro ratón robot. ¿En cuál de los tubos debería comenzar el robot para llegar al queso?': '3',
        }
    },
    {
        "title": "Género",
        "file":  "pre_mentores_genero.xlsx",
    }
]

# Nombre de las preguntas por el indice
# Esto se usará para aquellas preguntas que tengan subpreguntas
nombres_preguntas = {
    '10': '10. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Selección múltiple con múltiple respuesta)',
    '11': '11. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)',
    '13': '13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia (izquierda totalmente en desacuerdo y derecha totalmente de acuerdo)',
    '15': '15. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)',
    '16': '16. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos (izquierda totalmente des acuerdo y derecha totalmente de acuerdo)',
    '18': '18. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional',
    '20': '20. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:',
    '23': '''23. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo. Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando una que comienza con Trujillo, mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí.
¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.''',

}


def app():
    st.write("""# Pretest Mentores""")
    categoria = st.selectbox("Seleccione la categoría", files,
                             format_func=lambda itemArray: itemArray['title'])
    # Nombre del archivo con los datos
    file = f"data/limpios/pre_mentores/{categoria['file']}"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Identificación'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 18

    if file:
        data = load_data(file)
        datos = data.copy()
        chart_type = st.radio("Tipo de visualización ",
                              ("Barras", "Dispersión", "Cajas", "Tendencia"))
        pregunta, filtros_def, indices, lista_agrupadores, lista_grupo = filtros(
            datos, col_preguntas, chart_type, categoria, nombres_preguntas=nombres_preguntas, pregunta_con_numero=False)

        ejex, color, columna, fila = filtros_def
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)

        if color == "Eficacia":
            datos = graph_answer(datos, pregunta, categoria,
                                 pregunta_con_numero=False)

        orden_grupos = ["I"+str(x) for x in range(87)]

        if categoria['title'] == 'Conocimientos':
            datos[pregunta] = datos[pregunta].astype(str)

        category_orders = categories_order(
            set(datos[pregunta]), pregunta, orden_grupos)

        if lista_grupo != []:
            datos = datos.loc[datos.Grupo.isin(lista_grupo)]

        if len(datos) == 0:
            st.warning(
                "El / los grupos seleccionados no tienen datos para mostrar")
        elif (fila == "Grupo" or columna == "Grupo") and (len(datos.Grupo.unique()) > 10):
            st.warning(
                "Por favor use los filtros para seleccionar menos grupos")
        else:
            # Selecciona tipo de gráfica
            if chart_type == "Barras":
                """ Los diagramas de barra exigen agrupar la información antes de graficar """
                pivot = pivot_data(datos, indices, columna_unica)

                fig = bar_chart(columna_unica=columna_unica,
                                pivot=pivot, ejex=ejex, color=color,
                                fila=fila, columna=columna, indices=indices,
                                category_orders=category_orders)
            elif chart_type == "Cajas":
                fig = box_chart(columna_unica=pregunta,
                                pivot=datos, ejex=ejex, color=color,
                                fila=fila, columna=columna, indices=indices)
                fig.update_yaxes(col=1, title=None)
            elif chart_type == "Tendencia":
                fig = line_chart(columna_unica=columna_unica,
                                 pivot=datos, ejex=ejex, color=color, indices=indices,
                                 fila=fila, columna=columna,
                                 lista_agrupadores=datos.columns.tolist(),
                                 category_orders=category_orders)
            else:
                fig = scatter_chart(columna_unica=columna_unica,
                                    pivot=datos, ejex=ejex, color=color,
                                    fila=fila, columna=columna,
                                    lista_agrupadores=datos.columns.tolist(),
                                    category_orders=category_orders)

            # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
            fig.for_each_annotation(
                lambda a: a.update(text=a.text.split("=")[-1]))
            # Quita los nombres de los ejes (se ven feos cuando se divide por columnas)
            fig.update_yaxes(col=1, title=None)
            fig.update_xaxes(row=1, title=None)

            fig.update_layout(height=height)

            st.plotly_chart(fig, use_container_width=True, config=config_chart)
