import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


files = [
    {
        "title": "Autoeficacia",
        "file":  "post_avanzado_autoeficacia_C2.xlsx"
    },
    {
        "title": "Conocimientos",
        "file":  "post_avanzado_conocimientos_C2.xlsx",
        "respuestas": {
            "26": "Cerrar el centro para carros mientras la calidad del aire sea mala, muy mala, o extremadamente mala.",
            "27": "Esta función no imprime nunca nada",
            "28": "b",
            "29": "alfa, delta, gama, beta, épsilon",
            "30": "Cree que, si la condición se cumple, todo lo que sigue se va a ejecutar",
            "31": "Imagen 3",
            "32": "Cada uno tiene un número asignado y gana solamente si presiona su botón cuando sale este número",
            "34": "Imagen 3",
            "35": "x::3, y::5, z::10",
        }
    },
    {
        "title": "Género",
        "file":  "post_avanzado_genero_C2.xlsx"
    }
]

# Nombre de las preguntas por el indice
# Esto se usará para aquellas preguntas que tengan subpreguntas
nombres_preguntas = {
    '14': '14. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases?',
    '15': '15. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:',
    '17': '17. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:',
    '19': '19. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional:',
    '20': '20. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos:',
    '22': '22. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional.',
    '24': '24. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:',
}


def app():
    st.write("""# Posttest Avanzado C2""")

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
