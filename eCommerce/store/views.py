from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Brand, Product
from .serializers import BrandSerializers, ProductSerializers

# Create your views here.

# Brand
@api_view(["GET"])
def list_brand(request: Request):
    brands = Brand.objects.all()
    brand_data = BrandSerializers(instance=brands, many=True).data
    
    return Response({"msg" : "list of all brands", "brands" : brand_data})

@api_view(["POST"])
def add_brand(request: Request):
    brand_serializer = BrandSerializers(data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg": "couldn't add a brand store", "errors": brand_serializer.errors})

    return Response({"msg": "brand store added successfully"})

@api_view(["PUT"])
def brand_update(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg": "This is not found!"}, status=status.HTTP_404_NOT_FOUND)
    
    brand_serializer = BrandSerializers(instance=brand, data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg": "couldn't update", "errors": brand_serializer.errors})
    
    return Response({"msg": "brand updated successfully"})

@api_view(["DELETE"])
def brand_del(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : "The brand is not Found!"})

    return Response({"msg" : f"delete the brand {brand.title}"})





# Product
@api_view(["GET"])
def list_product(request: Request):
    products = Product.objects.all()
    product_data = ProductSerializers(instance=products, many=True).data
    
    return Response({"msg" : "list of all products", "products" : product_data})

@api_view(["POST"])
def add_product(request: Request):
    product_serializer = ProductSerializers(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg": "couldn't add a product to store", "errors": product_serializer.errors})

    return Response({"msg": "product added successfully"})

@api_view(["PUT"])
def product_update(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg": "couldn't update"})
    
    product_serializer = ProductSerializers(instance=product, data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg": "couldn't update", "errors": product_serializer.errors})
    
    return Response({"msg": "product updated successfully"})

@api_view(["DELETE"])
def product_del(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({"msg": "The product is not found!"})

    return Response({"msg": f"Delete the product {product.name}"})