from multiapp import MultiApp
from src.pages import graficador_horizontal
from src.pages import graficador_vertical
from src.pages import encuesta_genero_mentores
from src.pages import pretest_inicial
from src.pages import pretest_inicial_c2
from src.pages import posttest_inicial
from src.pages import prepost_inicial
from src.pages import pretest_avanzado
from src.pages import posttest_avanzado
from src.pages import prepost_avanzado
from src.pages import pretest_avanzado_c2
from src.pages import posttest_avanzado_c2
# from src.pages import encuesta_caracterizacion
from src.pages import caracterizacion_piloto_beta
from src.pages import pretest_piloto_beta
from src.pages import pretest_mentores
from src.pages import pretest_piloto_gamma
from src.pages import genero_y_actitudes_ambientales_piloto_beta
from src.pages import pretest_piloto_beta_analisis
from src.pages import pretest_piloto_gamma_analisis
from src.pages import quiz_inicial
from src.pages import quiz_avanzado
from src.pages import datos_app_partida
from src.pages import datos_app_insignia
from src.pages import datos_app_insignia_analisis
from src.pages import experiencia_piloto_gamma
from src.pages import experiencia_piloto_beta
from src.pages import greentic_insignias
from src.pages import greentic_partidas
from src.pages import pretest_eje_x

from src.preguntas.p1 import pregunta1
from src.preguntas.genero import genero_cohorte2
from src.preguntas.monitoreo import monitoreo

app = MultiApp('CFK 2021')

# Add all your application here
app.add_app("Pretest Inicial", pretest_inicial.app, "Inicial C1")
app.add_app("Posttest Inicial", posttest_inicial.app, "Inicial C1")
app.add_app("Pre - Post tests Inicial", prepost_inicial.app, "Inicial C1")
app.add_app("Quiz Inicial", quiz_inicial.app, "Inicial C1")
app.add_app("Eje X inicial - Avanzado", pretest_eje_x.app, "Inicial C1")

app.add_app("Pretest Avanzado", pretest_avanzado.app, "Avanzado C1")
app.add_app("Posttest Avanzado", posttest_avanzado.app, "Avanzado C1")
app.add_app("Pre - Post tests Avanzado", prepost_avanzado.app, "Avanzado C1")
app.add_app("Quiz Avanzado", quiz_avanzado.app, "Avanzado C1")

app.add_app("Pretest Inicial C2", pretest_inicial_c2.app, "Inicial C2")

app.add_app("Pretest Avanzado C2", pretest_avanzado_c2.app, "Avanzado C2")
app.add_app("Posttest Avanzado C2", posttest_avanzado_c2.app, "Avanzado C2")

app.add_app("Encuesta Género a Mentores",
            encuesta_genero_mentores.app, "Mentores")
app.add_app("Pretest Mentores", pretest_mentores.app, "Mentores")
# app.add_app("Encuesta Caracterización", encuesta_caracterizacion.app)

app.add_app("GreenTIC: Caracterización piloto beta",
            caracterizacion_piloto_beta.app, "Greentic")
app.add_app("GreenTIC: Pretest piloto beta",
            pretest_piloto_beta.app, "Greentic")
app.add_app("GreenTIC: Experiencia piloto beta",
            experiencia_piloto_beta.app, "Greentic")
app.add_app("GreentTIC Análisis: Pretest piloto beta",
            pretest_piloto_beta_analisis.app, "Greentic")

app.add_app("GreentTIC: Pretest piloto gamma",
            pretest_piloto_gamma.app, "Greentic")
app.add_app("GreenTIC: Género y actitudes ambientales",
            genero_y_actitudes_ambientales_piloto_beta.app, "Greentic")
app.add_app("GreenTIC: Experiencia piloto gamma",
            experiencia_piloto_gamma.app, "Greentic")
app.add_app("GreenTIC Análisis: Pretest piloto gamma",
            pretest_piloto_gamma_analisis.app, "Greentic")

# app.add_app("GreenTIC: Datos App partidas",
#			datos_app_partida.app, "Greentic")
# app.add_app("GreenTIC: Datos App insignias",
#			datos_app_insignia.app, "Greentic")
# app.add_app("GreenTIC Análisis: Datos App insignias",
#			datos_app_insignia_analisis.app, "Greentic")
app.add_app("GreenTIC: Datos App Insignias",
            greentic_insignias.app, "Greentic")
app.add_app("GreenTIC: Datos App Partidas", greentic_partidas.app, "Greentic")

app.add_app("Graficador formato horizontal",
            graficador_horizontal.app, "Herramientas")
app.add_app("Graficador formato vertical",
            graficador_vertical.app, "Herramientas")

# Preguntas

app.add_app("Género", genero_cohorte2.app, "Pregunta")
#app.add_app("Monitoreo", monitoreo.app, "Pregunta")
#app.add_app("Pregunta1", pregunta1.app, "Pregunta")
# The main app
app.run()
