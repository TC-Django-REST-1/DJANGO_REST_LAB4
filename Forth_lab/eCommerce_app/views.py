from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import  Brand ,Product
from .serializers import BrandSerializer,ProductSerializer

# Create your views here.


#BRAND#


@api_view(["POST"])
def create_brand(request: Request):
    brand_serializer = BrandSerializer(data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response(
            {
                "msg": "couldn't create a brand",
                "error": brand_serializer.errors
            },
            status=403
        )

    return Response(
        {
            "msg": "Brand created successfully."
        },
        status=201)
    


@api_view(["GET"])
def list_brands(request: Request):
    skip = int(request.query_params.get("skip"))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        brand_products = Brand.objects.filter(
            title__startswith=search_phrase)[skip:get]
    else:
        brand_products = Brand.objects.all()[skip:get]

    return Response(
        {
            "msg": f'list of {len(brand_products)} brands',
            "brands": BrandSerializer(instance=brand_products, many=True).data
        },
        status=status.HTTP_200_OK
    )


@api_view(["PUT"])
def update_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response(
            {
                "msg": f'Brand not found!.',
            },
            status=404
        )
    brand_serializer = BrandSerializer(instance=brand, data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response(
            {
                "msg": "Proces invalid.",
                "error": brand_serializer.errors
            },
            status=403
        )
    return Response(
        {
            "msg": f'Brand updated successfully',
        },
        status=status.HTTP_200_OK
    )


@api_view(["DELETE"])
def delete_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response(
            {
                "msg": f'brand not found.',
            },
            status=404
        )
    return Response(
        {
            "msg": f'{brand.title} brand deleted successfully .',
        },
        status=status.HTTP_200_OK
    )


@api_view(["POST"])
def create_product(request: Request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response(
            {
                "msg": "couldn't create a product.",
                "error": product_serializer.errors},status=403)

    return Response(
        {
            "msg": "Product created Successfully."
        },
        status=201
    )
    

@api_view(["GET"])
def list_brand_products(request: Request, brand_id):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response(
            {
                "msg": 'brand not found.',
            },
            status=404
        )

    brand_products = Product.objects.filter(brand=brand_id)[skip:get]
    return Response(
        {
            "msg": f'list of {len(brand_products)} products branded {brand.title}',
            "products": ProductSerializer(instance=brand_products, many=True).data
        },
        status=status.HTTP_200_OK
    )






#Products#


@api_view(["GET"])
def list_products(request: Request,):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 9))

    brand_products = Product.objects.all()[skip:get]

    return Response(
        {
            "msg": f'list of {len(brand_products)} products, total products {Product.objects.count()}',
            "products": ProductSerializer(instance=brand_products, many=True).data
        },
        status=status.HTTP_200_OK
    )


@api_view(["PUT"])
def update_product(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return Response(
            {
                "msg": f'product not found.',
            },
            status=404
        )
    product_serializer = ProductSerializer(instance=product, data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response(
            {
                "msg": " product does not exist!",
                "error": product_serializer.errors
            },
            status=404
        )
    return Response(
        {
            "msg": f'product updated successfully.',
        },
        status=status.HTTP_200_OK
    )


@api_view(["DELETE"])
def delete_product(request: Request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response(
            {
                "msg": f'the product is not found.',
            },
            status=404
        )
    return Response(
        {
            "msg": f'{product.title} product deleted successfully.',
        },
        status=status.HTTP_200_OK
    )

