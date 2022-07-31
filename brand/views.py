# from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from brand.models import Brand
from .serializers import BrandSerilizer
# Create your views here.


@api_view(['POST'])
def add_brand(request: Request) -> Response:

    brand = BrandSerilizer(data=request.data)
    
    if brand.is_valid():
        brand.save()
        return Response({"msg" : "added succefully!"})
    return Response({"msg": brand.errors})

@api_view(['GET'])
def get_brands(request: Request) -> Response:
    
    if "max" and "min" in request.query_params:

        maximumm = int(request.query_params.get("max"))
        minmumm = int(request.query_params.get("min"))

        brands = Brand.objects.all()[minmumm:maximumm]

    elif "search" in request.query_params:
        print("went")
        brand_title = request.query_params.get("search")
        brands = Brand.objects.filter(title=brand_title)

    else:

        brands = Brand.objects.order_by('-id').all()

    data = BrandSerilizer(brands, many=True).data

    return Response(data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_brand(request: Request, brand_id) -> Response:

    brand = Brand.objects.get(id=brand_id)

    data = BrandSerilizer(instance=brand, data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response({"msg": "updated succefully"}, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def delete_brand(request: Request, brand_id) -> Response:

    brand = Brand.objects.get(id=brand_id)

    brand.delete()

    return Response({"msg":"brand deleted succefully"})