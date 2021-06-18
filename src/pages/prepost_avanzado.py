import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


files = [
    {
        "title": "Autoeficacia",
        "file":  "prepost_avanzado_autoeficacia.xlsx"
    },
    {
        "title": "Conocimientos",
        "file":  "prepost_avanzado_conocimientos.xlsx",
        "respuestas": {
            "22": "Cerrar el centro para carros mientras la calidad del aire sea mala, muy mala, o extremadamente mala.",
            "23": "Esta función no imprime nunca nada",
            "24": "x ::2 * 3.14 * r  →  y ::x * r  → z ::h * x  → areaSuperficie :: y + z",
            "25": "alfa, delta, gama, beta, épsilon",
            "26": "Cree que, si la condición se cumple, todo lo que sigue se va a ejecutar",
            "27": "Imagen 3",
            "28": "Cada uno tiene un número asignado y gana solamente si presiona su botón cuando sale este número",
        }
    },
    {
        "title": "Género",
        "file":  "prepost_avanzado_genero.xlsx"
    }
]

# Nombre de las preguntas por el indice
# Esto se usará para aquellas preguntas que tengan subpreguntas
nombres_preguntas = {
    '10': '10. ¿Cuáles de las siguientes estrategias usted ha usado en sus clases? (Selección múltiple con múltiple respuesta)',
    '11': '11. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:',
    '13': '13. Por favor evalúe los siguientes enunciados de acuerdo con su experiencia:',
    '15': '15. Por favor evalúe las siguientes afirmaciones según qué tan de acuerdo está usted con enseñar las siguientes prácticas como objetivos de aprendizaje relacionados con el pensamiento computacional:',
    '16': '16. Por favor evalúe los siguientes enunciados de acuerdo con qué tan preparado(a) se siente para integrar el pensamiento computacional en sus cursos:',
    '18': '18. En una escala de 1 a 10 (donde 10 es muy a menudo), con qué frecuencia utilizarías las siguientes prácticas pedagógicas para enseñar pensamiento computacional.',
    '20': '20. Cuando un estudiante se enfrenta a una dificultad creando un programa y no sabe si está correcto, qué tan a menudo, en una escala de 1-10 (donde 10 es siempre), usted:',
}


def app():
    st.write("""# Pre - Post Avanzado (Datos relacionados)""")

    categoria = st.selectbox("Seleccione la categoría", files,
                             format_func=lambda itemArray: itemArray['title'])
    # Nombre del archivo con los datos
    file = f"data/limpios/{categoria['file']}"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Identificación'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 28

    if file:
        datos = load_data(file)
        chart_type = st.radio("Tipo de visualización ",
                              ("Barras", "Dispersión", "Cajas"))

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
            else:
                fig = scatter_chart(columna_unica=columna_unica,
                                    pivot=datos, ejex=ejex, color=color,
                                    fila=fila, columna=columna,
                                    lista_agrupadores=[
                                        pregunta]+lista_agrupadores,
                                    category_orders=category_orders)

            # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
            fig.for_each_annotation(
                lambda a: a.update(text=a.text.split("=")[-1]))
            fig.update_yaxes(col=1, title=None)
            fig.update_xaxes(row=1, title=None)

            fig.update_layout(height=height)

            st.plotly_chart(fig, use_container_width=True, config=config_chart)
