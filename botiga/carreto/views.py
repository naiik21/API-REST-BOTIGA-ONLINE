from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Carreto 
from .serializer import CarretoSerializer
from cataleg.models import LlistaProductes
from cataleg.serializer import LlistaProductesSerializer
from cataleg.serializer import LlistaProductesProducteSerializer
from cataleg.models import Producte
from cataleg.serializer import ProducteSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(["POST"])
def nouCarreto(request):
    carreto = CarretoSerializer(data=request.data)
    if carreto.is_valid():
        carreto.save()
        return Response(carreto.data, status=201)
    return Response(carreto.errors, status=400)



@api_view(["POST"])
def afegirProducte(request):
    serializer = LlistaProductesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


# Eliminar productes del carretó
@api_view(["DELETE"])
def eliminarProducte(request, pk):
    producte = get_object_or_404(LlistaProductes, id=pk)

    producte.delete()
    return Response(
        {"message": f"Producte amb id: {pk} eliminat"}, status=status.HTTP_200_OK
    )


# Eliminar tot el carretó
@api_view(["DELETE"])
def eliminarCarreto(request, pk):
    carreto = get_object_or_404(Carreto, id=pk)

    carreto.delete()
    return Response(
        {"message": f"Carreto amb id: {pk} eliminat"}, status=status.HTTP_200_OK
    )

# Modificar quantitat d'un producte
@api_view(["PUT"])
def modificarQuantitatProducte(request, pk):
    try:
        producte = LlistaProductes.objects.get(id=pk)
    except LlistaProductes.DoesNotExist:
        return Response(
            {"Error": "El producte no existeix"}, status=status.HTTP_404_NOT_FOUND
        )
    nova_quantitat = request.data.get("quantitat")

    if nova_quantitat is None:
        return Response(
            {"Error": "No s'ha proporcionat cap quantitat"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    producte.quantitat = nova_quantitat
    producte.save()

    serializer = LlistaProductesSerializer(producte)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def llistatProductesCarreto(request, pk):
    llista = LlistaProductes.objects.filter(carreto_id=pk)
    data_serializer = LlistaProductesProducteSerializer(llista, many=True)
    return Response({"data":data_serializer.data})


@api_view(['DELETE'])
def comprar(request, pk):
    try:
        carreto = Carreto.objects.get(id=pk)
    except carreto.DoesNotExist:
        return Response(status=404)
    serializer= CarretoSerializer(carreto, data=request.data ,partial=True)
    if serializer.is_valid():
        carreto.estaActiu = False
        serializer.save()  
        return Response(serializer.data)
    return Response(serializer.errors, status=400)