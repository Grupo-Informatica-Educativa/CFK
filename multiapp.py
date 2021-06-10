"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from src.pages import ejemplo2020

class MultiApp:

    def __init__(self, page_title):
        self.apps = []
        self.preguntas = []
        self.page_title = page_title
        st.set_page_config(
            page_title=page_title,
            layout="wide",
        )

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def add_pregunta(self, title, func):
        self.preguntas.append({
            "title": title,
            "function": func
        }
    )

    def run(self):
        st.sidebar.write(f'# {self.page_title}')
        ischecked = st.sidebar.checkbox('Habilitar herramientas:')
        if not ischecked:
            app = st.sidebar.radio(
                'Secciones:',
                self.apps,
                format_func=lambda app: app['title'])
            
            if len(self.preguntas) > 0:
                group_expander = st.sidebar.beta_expander(label='Graficas por Preguntas', expanded=False)
                with group_expander:
                    isPregunta_checked = st.checkbox('Habilitar')
                    if (isPregunta_checked):
                        app = st.radio(
                            'Seleccione una pregunta',
                            self.preguntas,
                            format_func=lambda app: app['title']
                        )

            app['function']()
        else:
            graph_expander = st.sidebar.beta_expander(label='Herramientas', expanded=True)
            with graph_expander:
                pages = [{
                    'title': 'Graficador',
                    'function': ejemplo2020.app
                }]
                app_expander = st.radio("Seleccione herramienta: ", pages, format_func=lambda app: app['title'])
            app_expander['function']()
        
        
