from rest_framework import serializers
from .models import Curso, Avaliacao
from django.db.models import Avg

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
        def validate_avaliacao(self,valor):
            if valor in range(1,6): #o ulitmo valor não é considerado!
                return valor
            raise serializers.ValidationError(' A avaliação deve estar entre 1 e 5')


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

    media_avaliacoes = serializers.SerializerMethodField()

    class Meta:
        model=Curso
        fields=[
            'id',
            'titulo',
            'url',
            'criacao',
            'ativo',
            'avaliacoes',
            'media_avaliacoes'
        ]
    def get_media_avaliacoes(self, obj): #Obj é o curso dentro da classe avaliacao
        media = obj.avaliacoes.aggregate(Avg('avaliacao')).get('avaliacao__avg') #função de agregadaco

        if media is None:
            return 0
        return round(media *2)/2  #padrão de média utilizado 
        





        