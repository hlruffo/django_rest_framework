# o trecho abaixo importa o token de .env
import os

import requests
from dotenv import load_dotenv

load_dotenv()


headers = {'Authorization': 'Token ' + os.environ["TOKEN"]}
url_cursos = os.environ["url_base_cursos"]
url_avaliacoes = os.environ["url_base_avaliacoes"]


resultado = requests.get(url=url_cursos, headers=headers)
# print(resultado.json())

# testando s eo endepoit está correto :
assert resultado.status_code == 200  # caso esteja tudo ok, não retorna nada!

# testando a quantidade de cursos registrados
assert resultado.json()['count'] == 5

# testando se o titulo do primeiro curso registrado está correto
assert resultado.json()['results'][0]['titulo'] == 'Curso de panetones 2'
