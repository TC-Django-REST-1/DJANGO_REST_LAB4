from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer



@api_view(['POST'])
def add_brand(request : Request):

    brand_serializer = BrandSerializer(data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "couldn't create a Brand", "errors" : brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "Brand Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_brands(request : Request):
    
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        brands = Brand.objects.filter(title=search_phrase)[skip:get]
    else:
        brands = Brand.objects.all()
        
    brand_data = BrandSerializer(instance=brands, many=True).data

    return Response({"msg" : "list of all brands", "Brands" : brand_data})




@api_view(['PUT'])
def update_brand(request : Request, brand_id):

    try:
        brands = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg" : "This brand is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    brand_serializer = BrandSerializer(instance=brands, data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : brand_serializer.errors})

    return Response({"msg" : "Brand updated successfully"})


@api_view(["DELETE"])
def delete_brand(request : Request, brand_id):

    try:
        brands = Brand.objects.get(id=brand_id)
        brands.delete()
    except Exception as e:
        return Response({"msg" : "The brand is not Found!"})

    return Response({"msg" : f"delete the following brand {brands.title}"})




#Product 


@api_view(['POST'])
def add_product(request : Request):

    product_serializer = ProductSerializer(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't create a product", "errors" : product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "product Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_products(request : Request):
    
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 3))
    
    products = Product.objects.all()[skip:get]
        
    products_data = ProductSerializer(instance=products, many=True).data

    return Response({"msg" : "list of all products", "Brands" : products_data})




@api_view(['PUT'])
def update_product(request : Request, product_id):

    try:
        products = Product.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg" : "This product is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    product_serializer = ProductSerializer(instance=products, data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : product_serializer.errors})

    return Response({"msg" : "product updated successfully"})


@api_view(["DELETE"])
def delete_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({"msg" : "The brand is not Found!"})

    return Response({"msg" : f"delete the following brand {product.brand}"})