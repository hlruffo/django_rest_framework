import os

import requests
from dotenv import load_dotenv

load_dotenv()
headers = {'Authorization': 'Token ' + os.environ["TOKEN"]}
cursos = requests.get('http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())


""" 
# get avaliações
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

print(avaliacoes.status_code)

# acessando os dados
print(avaliacoes.json())  # note que o formato da saída é um dicionario

# acessando a quantidade de registros
print(avaliacoes.json()['count'])

# acessando a proxima pagina de resultados
print(avaliacoes.json()['next'])

# acessando os resultados da pagina
print(avaliacoes.json()['results'])  # saida do tipo lista

# acessando um resulttado específico
print(avaliacoes.json()['results'][0])

# acessando o nome da pessoa que fez a ultima avaliação
print(avaliacoes.json()['results'][-1]['nome'])  # saida do tipo lista

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/1')
print(avaliacao.json())
 """
