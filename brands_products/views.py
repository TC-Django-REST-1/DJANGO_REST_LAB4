from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer

# Create your views here.


@api_view(["POST"])
def add_brand(request: Request):
  brand_serializer = BrandSerializer(data=request.data)
  if brand_serializer.is_valid():
    brand_serializer.save()
  else:
    return Response({ "msg": "Process failed!", "error": brand_serializer.errors }, status=403)
  return Response({ "msg": "Brand created successfully" }, status=201)

@api_view(["GET"])
def list_brands(request: Request):
  skip = int(request.query_params.get("skip", 0))
  get = int(request.query_params.get("get", 10))
  if "search" in request.query_params:
    search_phrase = request.query_params["search"]
    brands = Brand.objects.filter(title=search_phrase)[skip:get]
  else:
    brands = Brand.objects.all()
  return Response({ "msg" : "Brands list", "Brands" : BrandSerializer(instance=brands, many=True).data })

@api_view(["PUT"])
def update_brand(request: Request, brand_id):
  try:
    brand = Brand.objects.get(id=brand_id)
  except Exception as e:
    return Response({ "msg": 'Brand not found!' }, status=404)
  brand_serializer = BrandSerializer(instance=brand, data=request.data)
  if brand_serializer.is_valid():
    brand_serializer.save()
  else:
    return Response({ "msg": "Process failed!", "error": brand_serializer.errors }, status=403)
  return Response({ "msg": 'Brand updated successfully' })

@api_view(["DELETE"])
def delete_brand(request: Request, brand_id):
  try:
    brand = Brand.objects.get(id=brand_id)
    brand.delete()
  except Exception as e:
    print(e)
    return Response({ "msg": 'Process failed!' }, status=404)
  return Response({ "msg": f'{brand.title} deleted successfully' })

@api_view(["POST"])
def add_product(request: Request):
  product_serializer = ProductSerializer(data=request.data)
  if product_serializer.is_valid():
    product_serializer.save()
  else:
    return Response({ "msg": "Process failed!", "error": product_serializer.errors }, status=403)
  return Response({ "msg": "Product created successfully" }, status=201)

@api_view(["GET"])
def list_brand_products(request: Request, brand_id):
  skip = int(request.query_params.get("skip", 0))
  get = int(request.query_params.get("get", 3))
  try:
    brand = Brand.objects.get(id=brand_id)
  except Exception as e:
    print(e)
    return Response({ "msg": 'Process failed!' }, status=404)
  all_products = Product.objects.filter(brand=brand_id)[skip:get]
  return Response({ "msg": f'List of {len(all_products)} products branded {brand.title}', "products": ProductSerializer(instance=all_products, many=True).data })

@api_view(["GET"])
def list_products(request: Request):
  skip = int(request.query_params.get("skip", 0))
  get = int(request.query_params.get("get", 3))
  all_products = Product.objects.all()[skip:get]
  return Response({ "msg": f'List of {len(all_products)} products, total products {Product.objects.count()}', "products": ProductSerializer(instance=all_products, many=True).data })

@api_view(["PUT"])
def update_product(request: Request, product_id):
  try:
    product = Product.objects.get(id=product_id)
  except Exception as e:
    return Response({ "msg": 'Process faild!' }, status=404)
  product_serializer = ProductSerializer(instance=product, data=request.data)
  if product_serializer.is_valid():
    product_serializer.save()
  else:
    return Response({ "msg": "Process failed!", "error": product_serializer.errors }, status=403)
  return Response( { "msg": 'Product updated successfully' })

@api_view(["DELETE"])
def delete_product(request: Request, product_id):
  try:
    product = Product.objects.get(id=product_id)
    product.delete()
  except Exception as e:
    return Response({ "msg": 'Process failed!' }, status=404)
  return Response({ "msg": f'{product.title} deleted successfully' })