import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *

files = [
    {
        "title": "Autoeficacia",
        "file":  "pre_inicial_autoeficacia.xlsx"
    },
    {
        "title": "Conocimientos",
        "file":  "pre_inicial_conocimientos.xlsx"
    },
    {
        "title": "Género",
        "file":  "pre_inicial_genero.xlsx"
    }
]

def app():
    st.write("""# Pretest Inicial""")
    pregunta = st.selectbox("Seleccione la categoría",files,format_func=lambda itemArray: itemArray['title'])
    # Nombre del archivo con los datos
    file = f"data/limpios/{pregunta['file']}"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Identificación'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 28

    if file:
        datos = load_data(file)
        chart_type = st.radio("Tipo de visualización ",
                              ("Barras", "Dispersión", "Cajas"))

        pregunta, filtros_def, indices, lista_agrupadores, lista_grupo = filtros(
            datos, col_preguntas, chart_type)
        ejex, color, columna, fila = filtros_def
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)

        orden_grupos = ["I"+str(x) for x in range(87)]

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
            else:
                fig = scatter_chart(columna_unica=columna_unica,
                                    pivot=datos, ejex=ejex, color=color,
                                    fila=fila, columna=columna,
                                    lista_agrupadores=[pregunta]+lista_agrupadores,
                                    category_orders=category_orders)

            # Evita que los títulos de las subfiguras sean de forma VARIABLE=valor
            fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))
            # Quita los nombres de los ejes (se ven feos cuando se divide por columnas)
            fig.update_yaxes(col=1, title=None)
            fig.update_xaxes(row=1, title=None)

            fig.update_layout(height=height)

            st.plotly_chart(fig, use_container_width=True, config=config_chart)
