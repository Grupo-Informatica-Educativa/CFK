from multiapp import MultiApp
from src.pages import ejemplo2020
from src.pages import encuesta_genero_mentores

app = MultiApp('CFK 2021')

# Add all your application here
app.add_app("Ejemplo 2020", ejemplo2020.app)
app.add_app("Encuesta Género a Mentores", encuesta_genero_mentores.app)

# The main app
app.run()
