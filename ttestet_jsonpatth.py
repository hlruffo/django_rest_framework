import jsonpath
import requests

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes')

resultados = jsonpath.jsonpath(
    avaliacoes.json(), 'results')  # retorna uma lista !
print(resultados)

# primeira avaliação
primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeira)

# nome
# para que o resultado não seja uma lista basta inserir [0] apos os parenteses.
nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)

# avaliacao
nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
print(nota)

# curso
curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
print(curso_id)


# todos os nomes das pessoas que avaliaram os cursos.
nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
print(nomes)


# todas as avaliações ( notas)
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)
