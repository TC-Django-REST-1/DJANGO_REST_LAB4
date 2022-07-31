from unittest import skip
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Brand
from .serializers import ProductSerializer, BrandSerializer

# Create your views here.
'''

product


'''

@api_view(["POST"])
def create_product(request: Request):
    product_serializer = ProductSerializer(data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response(
            {
                "msg": "Product object invalid.",
                "error": product_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "Product created."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def read_products(request: Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    all_products = Product.objects.all()[skip:get]

    return Response(
        {
            "msg": f'list of {len(all_products)} products, total products {Product.objects.count()}',
            "products": ProductSerializer(instance=all_products, many=True).data
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
            status=status.HTTP_404_NOT_FOUND
        )
    product_serializer = ProductSerializer(instance=product, data=request.data)
    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response(
            {
                "msg": "Product object invalid.",
                "error": product_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )
    return Response(
        {
            "msg": f'product updated.',
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
                "msg": f'product not found.',
            },
            status=status.HTTP_404_NOT_FOUND
        )
    return Response(
        {
            "msg": f'{product.title} product deleted.',
        },
        status=status.HTTP_200_OK
    )


'''

Brand


'''


@api_view(["POST"])
def create_brand(request: Request):
    brand_serializer = BrandSerializer(data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response(
            {
                "msg": "Brand object invalid.",
                "error": brand_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )

    return Response(
        {
            "msg": "Brand created."
        },
        status=status.HTTP_201_CREATED
    )


@api_view(["GET"])
def read_brands(request: Request):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_products = Brand.objects.filter(
            title__startswith=search_phrase)[skip:get]
    else:
        all_products = Brand.objects.all()[skip:get]

    return Response(
        {
            "msg": f'list of {len(all_products)} brands',
            "brands": BrandSerializer(instance=all_products, many=True).data
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
                "msg": f'brand not found.',
            },
            status=status.HTTP_404_NOT_FOUND
        )
    brand_serializer = BrandSerializer(instance=brand, data=request.data)
    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response(
            {
                "msg": "Brand object invalid.",
                "error": brand_serializer.errors
            },
            status=status.HTTP_403_FORBIDDEN
        )
    return Response(
        {
            "msg": f'brand updated.',
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
            status=status.HTTP_404_NOT_FOUND
        )
    return Response(
        {
            "msg": f'{brand.title} brand deleted.',
        },
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
def read_brand_products(request: Request, brand_id):
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response(
            {
                "msg": f'brand not found.',
            },
            status=status.HTTP_404_NOT_FOUND
        )

    all_products = Product.objects.filter(brand=brand_id)[skip:get]
    return Response(
        {
            "msg": f'list of {len(all_products)} products branded {brand.title}',
            "products": ProductSerializer(instance=all_products, many=True).data
        },
        status=status.HTTP_200_OK
    )