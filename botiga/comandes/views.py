from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import OrdreSerializer
from .models import Ordre 
from clients.serializer import ClientSerializer
from clients.models import Client 

# Create your views here.
@api_view(['GET'])
def historial(request):
    listaComandes = Ordre.objects.all()
    data_serializer = OrdreSerializer(listaComandes, many=True)
    return Response({"data":data_serializer.data})

@api_view(['GET'])
def historialClient(request, pk):
    client = Client.objects.get(id=pk)
    
@api_view(['GET'])
def historialNoFin(request, pk):
    client = Client.objects.get(id=pk)