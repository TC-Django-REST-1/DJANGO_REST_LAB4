# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import ProductSerilizer
from rest_framework import status
from .models import Product
# Create your views here.


@api_view(["POST"])
def add_product(request: Request) -> Response:

    product = ProductSerilizer(data=request.data)
    
    if product.is_valid():
        product.save()
        return Response({"msg" : "added succefully!"})
    return Response({"msg": product.errors})


@api_view(['GET'])
def get_products(request: Request) -> Response:
    
    

    if "brand" in request.query_params :

        brand_id = int(request.query_params.get("brand"))
        products = Product.objects.filter(brand=brand_id)
        data = ProductSerilizer(products, many=True).data

    else:
        products = Product.objects.order_by('-id').all()
        data = ProductSerilizer(products, many=True).data

    return Response(data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_product(request: Request, product_id) -> Response:

    product = Product.objects.get(id=product_id)

    data = ProductSerilizer(instance=product, data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response({"msg": "updated succefully"}, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_product(request: Request, product_id) -> Response:

    product = Product.objects.get(id=product_id)

    product.delete()

    return Response({"msg":"product deleted succefully"})