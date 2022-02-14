from django.shortcuts import get_list_or_404, get_object_or_404
from importlib.util import resolve_name
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from rest_framework import status

from cars import serializers

# Create your views here.

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':

        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def car_detail(request, pk):
    if request.method == 'GET':
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    elif request.method == 'PUT':
        car = get_object_or_404(Car, pk=pk)
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

