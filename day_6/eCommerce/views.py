from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import status

from .models import Brand, Product
from .serializers import BrandSerilizer,ProductSerilizer


# BrandSerilizer
@api_view(['POST'])
def add_brand(request: Request):
    new_brand_serializer = BrandSerilizer(data=request.data)
    if new_brand_serializer.is_valid():
        new_brand_serializer.save()
    else:
        return Response({"msg" : "couldn't add a new brand", "errors" : new_brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "A new brand added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def brand_list(request: Request):

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 11))
        brands = Brand.objects.filter(title__startswith=search_phrase)[skip:get]
    else:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 11))
        brands = Brand.objects.order_by("-id").all()[skip:get]

    data = BrandSerilizer(brands, many=True).data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_brand(request: Request, brand_id):
    brand = Brand.objects.get(id = brand_id)
    data = BrandSerilizer(instance=brand, data=request.data)
    if data.is_valid():
        data.save()
        return Response({"msg" : "Brand updated successfully "}, status=status.HTTP_200_OK)
    else:
        return Response({"msg" : "couldn't update the brand", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_brand(request: Request, brand_id):
    try:
        brand = Brand.objects.get(id = brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : f"The brand with ID No:{brand_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"A brand with ID No:{brand_id} has been deleted successfully"}, status=status.HTTP_200_OK)




# ProductSerilizer
@api_view(['POST'])
def add_product(request: Request):
    new_product_serilizer = ProductSerilizer(data=request.data)
    if new_product_serilizer.is_valid():
        new_product_serilizer.save()
    else:
        return Response({"msg" : "couldn't add a new product", "errors" : new_product_serilizer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "A new product created successfully"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def product_list(request: Request):

    skip = int(request.query_params.get("skip", 1))
    get = int(request.query_params.get("get", 4))


    products = Product.objects.order_by("-id").all()[skip:get]
    data = ProductSerilizer(products, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_product(request: Request, product_id):
    product = Product.objects.get(id = product_id)
    data = ProductSerilizer(instance=product, data=request.data)
    if data.is_valid():
        data.save()
        return Response({"msg" : "Product updated successfully "}, status=status.HTTP_200_OK)
    else:
        return Response({"msg" : "couldn't update the product", "errors" : data.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def remove_product(request: Request, product_id):
    try:
        product = Brand.objects.get(id = product_id)
        product.delete()
    except Exception as e:
        return Response({"msg" : f"The product with ID No:{product_id} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"msg" : f"A product with ID No:{product_id} has been deleted successfully"}, status=status.HTTP_200_OK)




@api_view(['GET'])
def brand_products_list(request: Request, brand_title):
    try:
        products = Product.objects.filter(brand__title=brand_title) # filter all products using the brand model with any of its' field
        data = ProductSerilizer(products, many=True).data
        return Response(data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"msg" : f"The brand with ID No:{brand_title} is not Found!"}, status=status.HTTP_400_BAD_REQUEST)