from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Curso, Avaliacao
from .serializer import CursoSerializer, AvaliacaoSerializer

class CursoAPIView(APIView):
    """
    API de Cursos GEEK 
        """
    """
    O nome acima é exibido na tela desde que colocado com aspas !
    O código abaixo solicita as informações de todos os objetos Curso cadastrados
    serializa as informações
    retorna os dados serializados
    """
    
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status  = status.HTTP_201_CREATED)



class AvaliacaoAPIView(APIView):
    #API de avaliações
    def get(self, request):
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    def post( self, request):
        serializer=AvaliacaoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)