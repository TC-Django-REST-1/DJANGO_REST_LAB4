from itertools import product
from urllib import request
from .serializers import BrandSerializer, ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.shortcuts import render
from .models import Brand, Product
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def add_brand(request : Request):
    brand_serializer = BrandSerializer(data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "opps!  Brand could not created", "error": brand_serializer.errors},status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Brand Added Successfully!"},status=status.HTTP_201_CREATED)

@api_view(['POST'])
def add_product(request : Request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "opps!  product could not created", "error": product_serializer.errors},status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Product Added Successfully!"},status=status.HTTP_201_CREATED)

###############################################################
@api_view(['GET'])
def list_brand(request:Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 5))
    
    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        brands = Brand.objects.filter(title=search_phrase)[skip:get]
    else:
        brands = Brand.objects.all()[skip:get]
    brand = BrandSerializer(instance=brands, many=True).data

    return Response({"msg" : "List All Brands ","Brand" : brand}, status=status.HTTP_200_OK)

@api_view(['GET'])
def list_product(request:Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 5))

    products = Product.objects.all()[skip:get]
    product = ProductSerializer(instance=products, many=True).data

    return Response({"msg" : "List All products ", "product" : product}, status=status.HTTP_200_OK)


###############################################################
@api_view(['PUT'])
def update_brand(request:Request, brand_id):

    try:
        brand = Brand.objects.get(id = brand_id)
    except Exception :
        return Response({"msg" : "opss! brand is not found"}, status=status.HTTP_404_NOT_FOUND)

    brand_ser = BrandSerializer(instance=brand, data=request.data)

    if brand_ser.is_valid():
        brand_ser.save()
    else:
        return Response({"msg" : "opss! brand Couldn't update", "errors" : brand_ser.errors})

    return Response({"msg" : "Brand updated successfully"})

@api_view(['PUT'])
def update_product(request:Request,product_id):
    try:
        product = Product.objects.get(id = product_id)
    except Exception :
        return Response({"msg" : "opss! product is not found"}, status=status.HTTP_404_NOT_FOUND)

    product_ser = ProductSerializer(instance=product, data=request.data)

    if product_ser.is_valid():
        product_ser.save()
    else:
        return Response({"msg" : "opss! product Couldn't update", "errors" : product_ser.errors})

    return Response({"msg" : "Product updated successfully"})

###############################################################
@api_view(['DELETE'])
def delete_brand(request:Request, brand_id):
    brand = Brand.objects.get(id = brand_id)
    brand.delete()
    return Response({"msg" : "Brand Deleted successfully!"}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_product(request:Request, product_id):
    product = Product.objects.get(id =product_id)
    product.delete()
    return Response({"msg" : "Brand Deleted successfully!"}, status=status.HTTP_200_OK)

    
# ###############################################################

@api_view(['GET'])
def brand_all_product(request:Request, brand_id):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 5))
    try:
        brand = Brand.objects.get(id= brand_id)
    except Exception:
         return Response({"msg":"opss! brand not found"}, status=status.HTTP_404_NOT_FOUND)

    products = Product.objects.filter(brand= brand_id)[skip:get]
    product_data = ProductSerializer(instance=products, many=True).data
    response_data = {"Brand" : brand.title,"Products list of brand" : product_data}

    return Response(response_data, status=status.HTTP_200_OK)
