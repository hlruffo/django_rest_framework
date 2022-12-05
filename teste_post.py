import os

import requests
from dotenv import load_dotenv

load_dotenv()


headers = {'Authorization': 'Token ' + os.environ["TOKEN"]}
url_cursos = os.environ["url_base_cursos"]
url_avaliacoes = os.environ["url_base_avaliacoes"]

novo_curso = {
    "titulo": "Gerenciamento ágil de projetos com Scrum",
    "url": "http://www.hlruffo.com/agil"
}

resultado = requests.post(url=url_cursos, headers=headers, data=novo_curso)

# testando o codigo https de status ( para criação = 201 )
# o teste falha se a api estiver com endereço errado, for passadas as infos erradas,
# se já existir um curso com a url cadastrado
assert resultado.status_code == 201


# titulo do curso retornado na request é o nome informado ?
assert resultado.json()['titulo'] == novo_curso['titulo']
