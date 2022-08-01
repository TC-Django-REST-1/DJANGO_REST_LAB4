from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import productsSerializer
from rest_framework import status
from .models import products
# Create your views here.



@api_view(['GET'])
def get_products(request: Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        product_title = request.query_params.get("search")
        products = products.objects.filter(title=product_title)
        
    else:
        products = products.objects.all().order_by('-id')[skip:get]

    data = productsSerializer(products, many=True).data
    return Response({"msg" : "list of all products", "products" : data}, status=status.HTTP_200_OK)



@api_view(["POST"])
def add_product(request: Request):
    product = productsSerializer(data=request.data)
    
    if product.is_valid():
        product.save()
        return Response({"msg" : "product added succefully!"}, status=status.HTTP_201_CREATED)
    return Response({"msg" : "couldn't create a product", "errors" : product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)



@api_view(["PUT"])
def update_product(request: Request, product_id):
    product = products.objects.get(id=product_id)

    data = productsSerializer(instance=product, data=request.data,partial=True)

    if data.is_valid():
        data.save()
        return Response({"msg": "product updated succefully!"}, status=status.HTTP_200_OK)
    return Response({"msg" : "couldn't update", "errors" : product_serializer.errors})



@api_view(["DELETE"])
def delete_product(request: Request, product_id):
    product = products.objects.get(id=product_id)

    product.delete()

    return Response({"msg":"product deleted succefully!"})