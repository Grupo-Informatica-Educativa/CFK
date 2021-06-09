import streamlit as st
from src.utils.chart_funcs import *
from src.utils.helper_funcs import *


files = [
    {
        "title": "Autoeficacia",
        "file":  "pre_avanzado_autoeficacia.xlsx"
    },
    {
        "title": "Conocimientos",
        "file":  "pre_avanzado_conocimientos.xlsx"
    },
    {
        "title": "Género",
        "file":  "pre_avanzado_genero.xlsx"
    }
]

# Nombre de las preguntas por el indice
# Esto se usará para aquellas preguntas que tengan subpreguntas
nombres_preguntas = {
    
}

def app():
    st.write("""# Pretest Avanzado""")

    preguntas = st.selectbox("Seleccione la categoría", files,
                             format_func=lambda itemArray: itemArray['title'])
    # Nombre del archivo con los datos
    file = f"data/limpios/{preguntas['file']}"
    # Nombre de la columna cuyos datos son únicos para cada respuesta
    columna_unica = 'Identificación'
    # A partir de esta columna comienzan las preguntas (columnas de interés)
    col_preguntas = 29

    if file:
        datos = load_data(file)
        chart_type = st.radio("Tipo de visualización ",
                              ("Barras", "Dispersión", "Cajas"))

        pregunta, filtros_def, indices, lista_agrupadores, lista_grupos = filtros(
            datos, col_preguntas, chart_type, nombres_preguntas=nombres_preguntas)
        ejex, color, columna, fila = filtros_def
        height = st.slider(
            "Ajuste el tamaño vertical de la gráfica", 500, 1000)
        if preguntas['title'] == 'Conocimientos':
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
                                fila=fila, columna=columna, indices=indices)
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
