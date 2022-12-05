import os

import requests
from dotenv import load_dotenv

load_dotenv()


headers = {'Authorization': 'Token ' + os.environ["TOKEN"]}
url_cursos = os.environ["url_base_cursos"]
url_avaliacoes = os.environ["url_base_avaliacoes"]


resultado = requests.delete(url=f'{url_cursos}1/', headers=headers)
assert resultado.status_code == 204

assert.len(resultado.text) == 0
