from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs={
            'email':{ 'write_only':True}
        }
        model= Avaliacao
        fields =[
            'id',
            'curso',
            'nome',
            'email', #como email é dado sensivel o paramentro em extra kargs , faz com não exiba o email, apenas exija no ato de cadastro
            'comentario',
            'avaliacao',
            'criacao',
            'ativo'
        ]


class CursoSerializer(serializers.ModelSerializer):
    #nested relationships
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #hyperlinked Related Fiels
    """ 
        avaliacoes = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name ='avaliacao-detail')
 """
    #Primary Key Related Field
    avaliacoes =serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True)


    class Meta:
        model=Curso
        fields=[
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes'
        ]