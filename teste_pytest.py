import os

import requests
from dotenv import load_dotenv

load_dotenv()

url_avaliacoes = os.environ["url_base_avaliacoes"]


class TestCursos:
    headers = {'Authorization': 'Token ' + os.environ["TOKEN"]}
    url_cursos = os.environ["url_base_cursos"]

    def test_get_cursos(self):
        cursos = requests.get(url=self.url_cursos, headers=self.headers)

        assert cursos.status_code == 200

    def test_get_curso(self):
        curso = requests.get(url=f'{self.url_cursos}3/', headers=self.headers)

        assert curso.status_code == 200

    def test_post_curso(self):
        novo = {
            "titulo": "Curso bom",
            "url": "http://www.hlruffo.com/bom"
        }
        resposta = requests.post(
            url=self.url_cursos, headers=self.headers, data=novo)
        assert resposta.status_code == 201

    def test_put_curso(self):
        atualizado = {
            "titulo": "novo titulo atual",
            "url": "http://www.hlruffo.com/novo_atual"
        }
        resposta = requests.put(
            url=f'{self.url_cursos}4/', headers=self.headers, data=atualizado)
        assert resposta.status_code == 200
        assert resposta.json()['titulo'] == atualizado['titulo']

    """ def test_delete(self):
        resposta = requests.delete(
            url=f'{self.url_cursos}4/', headers=self.headers)
        assert resposta.status_code ==204 and len(resposta.text)==0
     """
