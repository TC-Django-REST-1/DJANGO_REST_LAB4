from itertools import product
from telnetlib import STATUS
from turtle import title
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Brand, Product
from .serializers import BrandSerializers, ProductSerializers
# Create your views here.

@api_view(['POST'])
def add_brand(request : Request):

    brand_Serializer = BrandSerializers(data=request.data)

    if brand_Serializer.is_valid():
        brand_Serializer.save()
    else:
        return Response({"msg" : "Couldn't create new brand", "errors":brand_Serializer.errors})
    
    return Response({"msg" : "Brand Added Successfully"})

@api_view(['GET'])
def list_brand(request : Request):
    
    skip = int(request.query_params.get("skip",0))
    get  = int(request.query_params.get("get",10))
    search_p = request.query_params["search"]

    brands = Brand.objects.all().filter(title=search_p)[skip:get]

    brand_data = BrandSerializers(instance=brands, many=True).data

    return Response({"msg" : "List of all brand", "Brand " : brand_data})

@api_view(["PUT"])
def update_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg" : "This brand is not found"})

    brand_Serializer = BrandSerializers(instance=brand, data=request.data)

    if brand_Serializer.is_valid():
        brand_Serializer.save()
        return Response({"msg" : "Brand is updated"})
    else:
        return Response({"msg" : "Couldn't update brand"})

@api_view(["DELETE"])
def delete_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
        msg = f"delete the following brand {brand.title}"
        brand.delete()
    except Exception as e:
        return Response({"msg" : "The brand is not found "})
    return Response({"msg":msg})
    


@api_view(['POST'])
def add_product(request : Request):

    product_Serializer = ProductSerializers(data=request.data)

    if product_Serializer.is_valid():
        product_Serializer.save()
    else:
        return Response({"msg" : "Couldn't create new product", "errors":product_Serializer.errors})
    
    return Response({"msg" : "Product Added Successfully"})

@api_view(['GET'])
def list_Product(request : Request):
    skip = int(request.query_params.get("skip",0))
    get  = int(request.query_params.get("get",10))
    brand_id = int(request.query_params.get("brand",-1))
    if brand_id != -1 :
        product = Product.objects.all().filter(brand=brand_id)[skip:get]
    else:
        product = Product.objects.all()[skip:get]

    product_data = ProductSerializers(instance=product, many=True).data

    return Response({"msg" : "List of all prodcuts", "Product " : product_data})

@api_view(["PUT"])
def update_product(request : Request, product_id):

    try:
        product = Brand.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg" : "This product is not found"})

    product_Serializer = ProductSerializers(instance=product, data=request.data)

    if product_Serializer.is_valid():
        product_Serializer.save()
        return Response({"msg" : "Product is updated"})
    else:
        return Response({"msg" : "Couldn't update product"})

@api_view(["DELETE"])
def delete_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        msg = f"delete the following product {product.name}"
        product.delete()
    except Exception as e:
        return Response({"msg" : "The product is not found "})
    return Response({"msg":msg})
    
