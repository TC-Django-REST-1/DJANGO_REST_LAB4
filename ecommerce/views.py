from django.shortcuts import render, get_object_or_404
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

    skip = int(request.query_params.get('skip', 0))
    get = int(request.query_params.get('get', 10))

    if 'search' in request.query_params:
        search = request.query_params['search']
        brands = Brand.objects.filter(title__startswith=search)[skip:get]

    brands = [
        {'id': brand.id, 'title': brand.title, 'description': brand.description, 'established_at': brand.established_at, 'city': brand.city}
        for brand in brands]
    return Response({'brands': brands})

@api_view(["GET"])
def list_product(request: Request):
    products = Product.objects.all()
    products = ProductSerilaizer(instance=products, many=True).data
    return Response({'products': products})


# put method
@api_view(['PUT'])
def update_brand(request: Request, id):
    title = request.data['title']
    description = request.data['description']
    established_at = request.data['established_at']
    city = request.data['city']

    brand = get_object_or_404(Brand, id=id)
    brand.title = title
    brand.description = description
    brand.established_at = established_at
    brand.city = city
    brand.save()

    return Response({'msg': 'Brand updated successfully'})


@api_view(['PUT'])
def update_product(request: Request, id):
    product = get_object_or_404(Product, id=id)
    product = ProductSerilaizer(instance=product, data=request.data)

    if product.is_valid():
        product.save()
    else:
        return Response({'msg': 'Could not update', 'errors': product.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({'msg': 'Product updated successfully'})


# delete method
@api_view(['DELETE'])
def delete_brand(request: Request, id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()
    return Response({'msg': 'Brand deleted successfully'})


@api_view(['DELETE'])
def deleted_product(request: Request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return Response({'msg': 'Product deleted successfully'})