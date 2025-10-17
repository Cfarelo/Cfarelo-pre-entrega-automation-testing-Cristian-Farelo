# pre-entrega-automation-testing--Cristian-Farelo-.

Proposito del proyecto: realizar testeos de prueba automatizados en el sitio "https://www.saucedemo.com"

tecnologias utilizadas: python - pytest - selenium web driver - git - conceptos de html y css

para ejecucion de test especificos utilizamos los comandos:

pytest tests\test_carrito.py
pytest tests\test_catalogo.py
pytest tests\test_login.py

en caso de querer ejecutar todos de forma detallada utilizamos:

pytest -v

para realizar un reporte html utilizamos el comando:

pytest -v --html=reporte.html