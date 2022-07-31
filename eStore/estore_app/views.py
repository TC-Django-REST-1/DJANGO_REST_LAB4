from hashlib import new
from urllib import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Brand,Product
from .serializers import BrandSerializer,ProductSerializer

# Brand...
# Add new brand 
@api_view(['POST'])
def new_brand(request:Request):

    Brand_serializer = BrandSerializer(data=request.data)

    if Brand_serializer.is_valid():
        Brand_serializer.save()
    else:
        return Response({"Message" : "Couldn't create a brand", "errors" : Brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"Message" : "Brand added successfully"}, status=status.HTTP_201_CREATED)

# Get all brands
@api_view(['GET'])
def read_brand(request:Request):

    all_brands = Brand.objects.all()
    brand_data = BrandSerializer(instance=all_brands, many=True).data

    response_data = {
        "Message" : "All Brands List",
        "Brand" : brand_data
    }

    return Response(response_data, status=status.HTTP_200_OK)


# Update brand by id 
@api_view(['PUT'])
def update_brand(request:Request, brand_id):

    try:
        brand = Brand.objects.get(id = brand_id)
    except Exception as e:
        return Response({"Message" : "This brand is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    brand_serializer = BrandSerializer(instance=brand, data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"Message" : "Couldn't update", "errors" : brand_serializer.errors})

    return Response({"Message" : "Brand updated successfully"})

# Delete brand by id 
@api_view(['DELETE'])
def delete_brand(request:Request, brand_id):
    
    brand = Brand.objects.get(id = brand_id)
    brand.delete()

    response_data = {
        "Message" : "Brand Information Deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)

# Limited list of brands
@api_view(["GET"])
def limited_list_brand(request : Request):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 2))

    brands_list = Brand.objects.all()[skip:get]

    brands = BrandSerializer(instance=brands_list, many=True).data

    res_data = {
        "msg" : "Limited list of Brands",
        "Brand" : brands
    }

    return Response(res_data, status=status.HTTP_200_OK)

# ***************************************************** #

# Product...
# Add new brand 
@api_view(['POST'])
def new_product(request:Request):

    Product_serializer = ProductSerializer(data=request.data)
    if Product_serializer.is_valid():
        Product_serializer.save()

    else:
        return Response({"Message" : "Couldn't create a product", "errors" : Product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({ "Message" : "Added a Product Successfully"}, status=status.HTTP_201_CREATED)

# Get all products 
@api_view(['GET'])
def read_product(request:Request):
    
    all_products = Product.objects.all()
    product_data = ProductSerializer(instance=all_products, many=True).data

    response_data = {
        "Message" : "All Products List",
        "Brand" : product_data
    }

    return Response(response_data, status=status.HTTP_200_OK)

# Update product by id 
@api_view(['PUT'])
def update_product(request:Request,product_id):

    try:
        product = Product.objects.get(id = product_id)
    except Exception as e:
        return Response({"Message" : "This product is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    product_serializer = ProductSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"Message" : "Couldn't update", "errors" : product_serializer.errors})

    return Response({"Message" : "Product updated successfully"})

# Delete product by id 
@api_view(['DELETE'])
def delete_product(request:Request, product_id):
    
    product = Product.objects.get(id = product_id)
    product.delete()

    response_data = {
        "Message" : "Product Information Deleted!",
    }
    return Response(response_data, status=status.HTTP_200_OK)

# Limited list of products
@api_view(["GET"])
def limited_list_product(request : Request):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 2))

    products_list = Product.objects.all()[skip:get]

    products = ProductSerializer(instance=products_list, many=True).data

    res_data = {
        "msg" : "Limited list of Products",
        "Products" : products
    }

    return Response(res_data, status=status.HTTP_200_OK)

# Get all products of spcific brand 
@api_view(['GET'])
def products_of_brand(request:Request, brand_id):

    brand = Brand.objects.get(id= brand_id)
    products = Product.objects.filter(brand= brand_id)
    product_data = ProductSerializer(instance=products, many=True).data

    response_data = {
        "Brand" : brand.title,
        "Products" : product_data
    }

    return Response(response_data, status=status.HTTP_200_OK)

# ***************************************************** #

#Search
@api_view(["GET"])
def search(request : Request , brand_title):
    try:
        brand = Brand.objects.get(title = brand_title)
    except Exception as e:
        return Response({"Message" : "This brand title is not found"}, status=status.HTTP_404_NOT_FOUND)

    brands = Brand.objects.filter(title = brand_title)
    brands_list = BrandSerializer(instance=brands, many=True).data

    res_data = {
        "Search of brand title" : brand_title,
        "Brand" : brands_list
        }

    return Response(res_data, status=status.HTTP_200_OK)

