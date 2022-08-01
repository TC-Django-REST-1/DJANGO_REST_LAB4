from django.shortcuts import render
from .models import Brand, Product
from .serializers import ProductSerilaizer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view


# post method
@api_view(["POST"])
def add_brand(request: Request):
    title = request.data['title']
    description = request.data['description']
    established_at = request.data['established_at']
    city = request.data['city']

    brand = Brand(title=title, description=description, established_at=established_at, city=city).save()

    return Response({'msg': "Brand added successfully"})

@api_view(["POST"])
def add_product(request: Request):
    product_serializer = ProductSerilaizer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({'msg': 'Could not create product', 'errors': product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
    return Response({'msg': 'Product added successfully'}, status=status.HTTP_201_CREATED)


# get method
@api_view(["GET"])
def list_brand(request: Request):
    brands = Brand.objects.all()
    brands = [
        {'id': brand.id, 'title': brand.title, 'description': brand.description, 'established_at': brand.established_at, 'city': brand.city}
        for brand in brands]
    return Response({'brands': brands})

@api_view(["GET"])
def list_product(request: Request):
    products = Product.objects.all()
    products = ProductSerilaizer(instance=products, many=True).data
    return Response({'products': products})
