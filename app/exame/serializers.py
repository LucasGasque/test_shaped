from .models import Exame, Paciente
from rest_framework import serializers


class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ["nome", "idade", "endereco"]


class ExameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Exame
        fields = ["nome_profissional", "data_exame", "peso", "altura", "paciente"]
