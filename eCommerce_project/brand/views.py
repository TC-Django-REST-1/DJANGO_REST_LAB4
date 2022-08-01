from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from brand.models import brands
from .serializers import brandsSerializer
# Create your views here.



@api_view(['GET'])
def get_brands(request: Request):
    skip = int(request.query_params.get("skip"))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        brand_title = request.query_params.get("search")
        brands = brands.objects.filter(title=brand_title)
        
    else:
        brands = brands.objects.all().order_by('-id')[skip:get]

    data = brandsSerializer(brands, many=True).data
    return Response({"msg" : "list of all brands", "brands" : data}, status=status.HTTP_200_OK)



@api_view(['POST'])
def add_brand(request: Request):
    brand = brandsSerializer(data=request.data)
    
    if brand.is_valid():
        brand.save()
        return Response({"msg" : "brand added succefully!"}, status=status.HTTP_201_CREATED)
    return Response({"msg" : "couldn't create a brand", "errors" : brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)



@api_view(["PUT"])
def update_brand(request: Request, brand_id):
    brand = brands.objects.get(id=brand_id)
    data = brandsSerializer(instance=brand, data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response({"msg": "brand updated succefully!"}, status=status.HTTP_200_OK)
    return Response({"msg" : "couldn't update the brand", "errors" : brand_serializer.errors})


@api_view(["DELETE"])
def delete_brand(request: Request, brand_id):
    brand = brands.objects.get(id=brand_id)
    brand.delete()

    return Response({"msg":"brand deleted succefully!"})