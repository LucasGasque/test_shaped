from rest_framework import viewsets

from exame.serializers import ExameSerializer, PacienteSerializer
from .models import Paciente, Exame

# Create your views here.


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


class ExameViewSet(viewsets.ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer
