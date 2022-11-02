from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Drink
from .serializers import DrinkSerializer

# Create your views here.
@api_view(['GET', "POST"])
def drink_list(request, format=None):
    method = request.method
    if method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)

    
    elif method == 'POST':
        newData = DrinkSerializer(data=request.data)
        if newData.is_valid():
            newData.save()
            return Response(newData.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_details(request, id, format=None):
    method = request.method

    target = None
    try:
        target = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Drink Not found"})
    if method == 'GET':
        serializer = DrinkSerializer(target)
        return Response(serializer.data)

    elif method == 'PUT':
        serializer = DrinkSerializer(target, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif method == 'DELETE':
        target.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
