from operator import is_
from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models.functions import Lower
from rest_framework import status
from django.db.models import Q

from .models import Brand, Product
from .serializers import ProductSerializer, BrandSerializer
from eCommerce import serializers


@api_view(["POST"])
def add_brand(request: Request):

    new_Product = BrandSerializer(data=request.data)
    if new_Product.is_valid():
        new_Product.save()
    else:
        print(request.data["title"])
        return Response({
            "msg": new_Product.errors, "details": (new_Product.data.values())
        }, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({
        "msg": f"create a new brand with title {{ {new_Product.data.get('title')} }} Successfully"
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_brand(request: Request):

    # returns the total count of Brand in the database, for testing only
    print(Brand.objects.count())
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_brands = Brand.objects.filter(
            title__contains=search_phrase).values()
    else:
        all_brands = Brand.objects.order_by(Lower("title"))

    res_data = {
        "msg": "A list of All brands",
        "brands": all_brands.values()[skip:get]
    }
    return Response(res_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_brand(request: Request, brand_title: str):

    data_obj = Brand.objects.get(title=brand_title)
    data = BrandSerializer(data_obj, request.data)
    if data.is_valid():
        print(data)
        data.save()
        return Response({"msg": "Your book is updated !"})
    else:
        print(data.errors)
        return Response({"msg": data.errors})


@api_view(["DELETE"])
def delete_brand(request: Request, brand_title):

    try:
        brand = Brand.objects.get(title=brand_title)
        brand.delete()
    except Exception as e:
        return Response({"msg": f"The brand {brand_title} is not Found!"})

    return Response({"msg": f"delete the following brand {brand_title}"})


@api_view(['POST'])
def add_Product(request: Request):

    new_Product = ProductSerializer(data=request.data)
    if new_Product.is_valid():
        new_Product.save()
    else:
        print(request.data["brand"])
        return Response({
            "msg": new_Product.errors, "details": (new_Product.data.values())
        }, status=status.HTTP_406_NOT_ACCEPTABLE)
    print(new_Product.data.get('name'))
    # {{ {new_Product.data.get('name')} }} {request.data.get['brand']}
    return Response({
        "msg": f"create a new brand with brand  with name Successfully"
    }, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_Products(request: Request):

    # returns the total count of Products in the database, for testing only
    print(Product.objects.count())

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_Product = Product.objects.filter(Q(brand=search_phrase))
        remove_id = all_Product.values()[0]
        res_data = {
            "msg": f"A list of All Products of the brand {search_phrase} ",
            "brands": remove_id
        }
    else:
        all_Product = Product.objects.order_by(Lower("name"))

        # serializer = all_Product.exclude('brand_id').values()
        remove_id = all_Product.values()
        
        res_data = {
            "msg": "A list of All Product",
            "Product": remove_id
        }

    return Response(res_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_product(request: Request, product_id: str):

    data_obj = Product.objects.get(id=product_id)
    data = ProductSerializer(data_obj, request.data)
    if data.is_valid():
        print(data)
        data.save()
        return Response({"msg": "Your book is updated !"})
    else:
        print(data.errors)
        return Response({"msg": data.errors})


@api_view(["DELETE"])
def delete_product(request: Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        print(e)
        return Response({"msg": f"The product {product_id} is not Found!"})

    return Response({"msg": f"delete the following product {product_id}"})
