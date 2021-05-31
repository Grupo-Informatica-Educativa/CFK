"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
from src.pages import ejemplo2020

class MultiApp:
    # From  https://github.com/upraneelnihar/streamlit-multiapps
    #       https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4
    """Framework for combining multiple streamlit applications.
    Usage:
        def foo():
            st.title("Hello Foo")
        def bar():
            st.title("Hello Bar")
        app = MultiApp()
        app.add_app("Foo", foo)
        app.add_app("Bar", bar)
        app.run()
    It is also possible keep each application in a separate file.
        import foo
        import bar
        app = MultiApp()
        app.add_app("Foo", foo.app)
        app.add_app("Bar", bar.app)
        app.run()
    """

    def __init__(self, page_title):
        self.apps = []
        self.page_title = page_title
        st.set_page_config(
            page_title=page_title,
            layout="wide",
        )

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.write(f'# {self.page_title}')
        app = st.sidebar.radio(
            'Secciones:',
            self.apps,
            format_func=lambda app: app['title'])
        ischecked = st.sidebar.checkbox('Habilitar herramientas:')
        if not ischecked:
            app['function']()
        else:
            graph_expander = st.sidebar.beta_expander(label='Herramientas')
            with graph_expander:
                pages = [{
                    'title': 'Graficador',
                    'function': ejemplo2020.app
                }]
                app_expander = st.radio("Seleccione herramienta: ", pages, format_func=lambda app: app['title'])
            app_expander['function']()
        
        
