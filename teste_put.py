import os

import requests
from dotenv import load_dotenv

load_dotenv()


headers = {'Authorization': 'Token ' + os.environ["TOKEN"]}
url_cursos = os.environ["url_base_cursos"]
url_avaliacoes = os.environ["url_base_avaliacoes"]


resultado = requests.put(url=url_cursos, headers=headers)

curso_atualizado = {
    "titulo": "Novo Curso ",
    "url": "http://hlruffo.com/novo"
}

# buscando o curso id 1
#curso = requests.get(url=f'{url_cursos}1/', headers=headers)
# print(curso.json())

# atualizando o curso da id 1
resultado = requests.put(url=f'{url_cursos}1/',
                         headers=headers, data=curso_atualizado)

# testando o status
assert resultado.status_code == 200

# testando o titulo
#assert resultado.json()['titulo'] == curso_atualizado['titulo']

curso = requests.get(url=f'{url_cursos}1/', headers=headers)
print(curso.json())
