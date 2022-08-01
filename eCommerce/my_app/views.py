from turtle import title
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status

from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer

# Create your views here.


### Brand Views

@api_view(["GET"])
def list_brand(request: Request):
    brands = Brand.objects.all()

    skip = int(request.query_params.get("skip"))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        brands = Brand.objects.filter(title__startswith=search_phrase)[skip:get]
    else:
        brands = Brand.objects.all().order_by('established_at')[skip:get]

    brands_data = BrandSerializer(instance=brands, many=True).data

    return Response({"msg": "list of all brands", "brands": brands_data})

@api_view(['POST'])
def add_brand(request: Request):
    brand_serializer = BrandSerializer(data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else: 
        return Response({"msg": "couldn't create brand", "errors": brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg": "brand created successfuly!"}, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
def update_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg": "This brand does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    brand_serializer = BrandSerializer(instance=brand, data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else: 
        return Response({"msg": "couldn't update", "errors": brand_serializer.errors})

    return Response({"msg": "brand updated successfuly!"})

@api_view(["DELETE"])
def delete_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg": "brand is not found!"})

    return Response({"msg": f"{brand.title} brand has been deleted!!"})



#### Product Views
@api_view(["GET"])
def get_product_of_brand(request: Request, brand_title):
    try:
        brand = Brand.objects.get(title=brand_title)
    except Exception as e:
        return Response({"msg": "the brand in not found!!"}, status=status.HTTP_404_NOT_FOUND)

    brand_data = BrandSerializer(instance=brand).data
    return Response({"msg": f"list of {brand_title} products!", "products": brand_data})

@api_view(['POST'])
def add_product(request: Request):
    product_serializer = ProductSerializer(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else: 
        return Response({"msg": "couldn't create product", "errors": product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg": "product created successfuly!"}, status=status.HTTP_201_CREATED)

@api_view(["GET"])
def list_product(request: Request):
    products = Product.objects.all()
    products_data = ProductSerializer(instance=products, many=True).data

    return Response({"msg": "list of all products", "products": products_data})


@api_view(["PUT"])
def update_product(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg": "This product does not exist!"}, status=status.HTTP_404_NOT_FOUND)

    product_serializer = ProductSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else: 
        return Response({"msg": "couldn't update", "errors": product_serializer.errors})

    return Response({"msg": "product updated successfuly!"})

@api_view(["DELETE"])
def delete_product(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({"msg": "product is not found!"})

    return Response({"msg": f"{product.name} product has been deleted!!"})
