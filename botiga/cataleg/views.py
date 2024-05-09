from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProducteSerializer
from .models import Producte 

# Create your views here.

@api_view(['GET'])
def productes(request):
    listaProductes = Producte.objects.all()
    data_serializer = ProducteSerializer(listaProductes, many=True)
    return Response({"data":data_serializer.data})


@api_view(['GET'])
def producte(request, pk):
    producte = Producte.objects.get(id=pk)
    data_serializer = ProducteSerializer(producte, many=False)
    return Response({"data":data_serializer.data})

@api_view(['POST'])
def nouProducte(request):
    serializer=ProducteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT'])
def editaProducte(request, pk):
    try:
        producte = Producte.objects.get(id=pk)
    except Producte.DoesNotExist:
        return Response(status=404)
    if request.method == 'GET':
        serializer=ProducteSerializer(producte)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer= ProducteSerializer(producte, data=request,partial=True)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.errors, status=400)
    