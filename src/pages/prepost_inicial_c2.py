import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


files = [
    {
        "title": "Autoeficacia",
        "file":  "prepost_inicial_autoeficacia_c2.xlsx"
    },
    {
        "title": "Conocimientos",
        "file":  "prepost_inicial_conocimientos_c2.xlsx",
        "respuestas": {
            "26": "3",
            "27": "El programa no funciona, debe capturar nuevamente el valor de la temperatura luego de encender el ventilador",
            "28": "6",
            "29": "10",
            "30": "II y III",
            "31": "La segunda expresión es verdadera si “(a O b)” es verdadero",
            "32": "Imagen 3",
            "33": "La botella B debe ser verde",
            "34": "Está equivocada, el resultado es 120.",
        }
    },
    {
        "title": "Género",
        "file":  "prepost_inicial_genero_c2.xlsx"
    }
]

# Nombre de las preguntas por el indice
# Esto se usará para aquellas preguntas que tengan subpreguntas
nombres_preguntas = {
    '12': '12. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?',
    '13': '13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia',
    '15': '15. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:',
    '17': '17. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional',
    '18': '18. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos',
    '20': '20. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional.',
    '22': '22. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:',
    '24': '''24. La docente Margarita decidió hacer que sus estudiantes de segundo de primaria utilicen los computadores del colegio para predecir el clima de una semana (temperatura,
    precipitaciones, y viento). Cada estudiante debe dibujar cómo se verá el clima en la ciudad en dicha semana. Margarita, creó un archivo compartido donde los estudiantes ingresarán la información. Luego tomaron las predicciones de modelos de Internet y los ingresaron en el mismo documento compartido. Durante una semana tomaron los datos reales, y luego, proyectaron en el tablero los datos predichos por los estudiantes,
    los del modelo de Internet, y los datos reales. Al finalizar, Margarita les mostró a los estudiantes cómo hacer un gráfico para comparar los diferentes datos. ¿Está Margarita desarrollando el pensamiento computacional de sus estudiantes? Seleccione todas las respuestas que considere correctas.''',
    '25': '''25. La cafetería del colegio empacó almuerzos iguales para todos los estudiantes, menos los de Juan Arias y María Vásquez que no pueden comer huevo.
    Los almuerzos están marcados con el apellido de los estudiantes y organizados alfabéticamente. Para verificar que su almuerzo cumple con la restricción alimenticia María con ayuda de su profesor buscan en las cajas. María sabe que su almuerzo debe estar al final, así que busca hasta que encuentre una caja que comience por una letra cerca de la V. Cuando encuentra una que comienza con Trujillo,
    mira el último almuerzo de esa caja y se da cuenta que termina en Zapata. Así, María se da cuenta que su almuerzo debe estar allí. ¿Está María usando el pensamiento computacional para encontrar su almuerzo? Seleccione todas las respuestas que considere correctas.''',
}


def app():
    st.write("""# Pre - Post Inicial C2 (Datos relacionados)""")

    chart_type = st.radio("Tipo de visualización ",
                          ("Barras", "Dispersión", "Cajas", "Tendencia"))

    categoria = st.selectbox("Seleccione la categoría", files,
                             format_func=lambda itemArray: itemArray['title'])
    # Nombre del archivo con los datos
    file = f"data/limpios/{categoria['file']}"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Identificación'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 25

    if file:
        datos = load_data(file)

        pregunta, filtros_def, indices, lista_agrupadores, lista_grupos = filtros(
            datos, col_preguntas, chart_type, categoria, nombres_preguntas=nombres_preguntas)

        ejex, color, columna, fila = filtros_def
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)

        if color == "Eficacia":
            datos = graph_answer(datos, pregunta, categoria)

        if categoria['title'] == 'Conocimientos':
            if pregunta == 'Puntaje Conocimiento':
                datos[pregunta] = datos[pregunta].astype(float)
            else:
                datos[pregunta] = datos[pregunta].astype(str)

        orden_grupos = ["A"+str(x) for x in range(36)]
        category_orders = categories_order(
            set(datos[pregunta]), pregunta, orden_grupos)

        if lista_grupos != []:
            datos = datos.loc[datos.Grupo.isin(lista_grupos)]
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
                                fila=fila, columna=columna, indices=indices, category_orders=category_orders)
                fig.update_yaxes(col=1, title=None)
            elif chart_type == "Tendencia":
                fig = line_chart(columna_unica=columna_unica,
                                 pivot=datos, ejex=ejex, color=color, indices=datos.columns.tolist(),
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
            fig.update_yaxes(col=1, title=None)
            fig.update_xaxes(row=1, title=None)

            fig.update_layout(height=height)

            st.plotly_chart(fig, use_container_width=True, config=config_chart)
