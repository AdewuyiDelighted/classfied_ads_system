from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ad_infomation.models import Ads
from ad_infomation.serializers import AdsSerializer


# Create your views here.


@api_view(['POST'])
def create_ads(request):
    if request.method == 'POST':
        serializer = AdsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_ads(request):
    if request.method == 'GET':
        all_ads = Ads.objects.all()
        serializer = AdsSerializer(all_ads, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_all_ads(request, pk):
    ads = get_object_or_404(Ads, id=pk)
    if request.method == 'GET':
        serializer = AdsSerializer(ads)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_ads(request, pk):
    ads = get_object_or_404(Ads, id=pk)
    if request.method == 'DELETE':
        ads.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_ads(request, pk):
    ads = get_object_or_404(Ads,id=pk)
    if request.method == 'PUT':
        serializer = AdsSerializer(ads, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)

