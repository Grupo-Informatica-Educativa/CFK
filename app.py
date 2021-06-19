from multiapp import MultiApp
from src.pages import ejemplo2020
from src.pages import encuesta_genero_mentores
from src.pages import pretest_inicial
from src.pages import posttest_inicial
from src.pages import prepost_inicial
from src.pages import pretest_avanzado
from src.pages import posttest_avanzado
from src.pages import prepost_avanzado
from src.pages import encuesta_caracterizacion
from src.pages import caracterizacion_piloto_beta
from src.pages import pretest_piloto_beta
from src.pages import pretest_mentores
from src.pages import pretest_piloto_gamma
from src.pages import genero_y_actitudes_ambientales_piloto_beta

from src.preguntas.p1 import pregunta1

app = MultiApp('CFK 2021')

# Add all your application here
app.add_app("Pretest Inicial", pretest_inicial.app, "Inicial")
app.add_app("Posttest Inicial", posttest_inicial.app, "Inicial")
app.add_app("Pre - Post tests Inicial", prepost_inicial.app, "Inicial")

app.add_app("Pretest Avanzado", pretest_avanzado.app, "Avanzado")
app.add_app("Posttest Avanzado", posttest_avanzado.app, "Avanzado")
app.add_app("Pre - Post tests Avanzado", prepost_avanzado.app, "Avanzado")

app.add_app("Encuesta Género a Mentores",
            encuesta_genero_mentores.app, "Mentores")
app.add_app("Pretest Mentores", pretest_mentores.app, "Mentores")
#app.add_app("Encuesta Caracterización", encuesta_caracterizacion.app)

app.add_app("GreenTIC: Caracterización piloto beta",
            caracterizacion_piloto_beta.app, "Greentic")
app.add_app("GreenTIC: Pretest piloto beta",
            pretest_piloto_beta.app, "Greentic")
app.add_app("GreentTIC: Pretest piloto gamma",
            pretest_piloto_gamma.app, "Greentic")
app.add_app("GreenTIC: Género y actitudes ambientales",
            genero_y_actitudes_ambientales_piloto_beta.app, "Greentic")

app.add_app("Graficador", ejemplo2020.app, "Herramientas")
# The main app
app.run()
