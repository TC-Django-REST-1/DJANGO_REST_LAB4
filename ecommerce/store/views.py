from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status

from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer

# Create your views here.




# Brand CRUD

@api_view(['POST'])
def create_brand(request : Request):
    
    brand_ser = BrandSerializer(data=request.data)
    
    if brand_ser.is_valid():
        brand_ser.save()
    else:
        return Response({"msg" : "Brand couldn't be created.", "errors" : BrandSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Brand created Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_brands(request : Request):

    if "skip" in request.query_params and "get" in request.query_params:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))

        brand = Brand.objects.all()[skip:get]
        brand_data = BrandSerializer(instance=brand, many=True).data
    else:
        brand = Brand.objects.all()
        brand_data = BrandSerializer(instance=brand, many=True).data

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        brand = Brand.objects.filter(title=search_phrase)
        brand_data = BrandSerializer(instance=brand, many=True).data

    return Response({"msg" : "list of all brands", "brands" : brand_data})

@api_view(['GET'])
def get_brand_by_name(request : Request, brand_name):
    
    try:
        brand = Brand.objects.get(title=brand_name)
        brand_data = BrandSerializer(instance=brand).data

        return Response({"msg" : "brand found", "brand" : brand_data})
    except:
        return Response({"msg" : "Brand not found !!"})
    
    
@api_view(['PUT'])
def update_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
    except:
        return Response({"msg" : "Brand couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
    
    brand_serializer = BrandSerializer(instance=brand, data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "Brand couldn't be updated", "errors" : brand_serializer.errors})

    return Response({"msg" : "Brand updated Successfully!"})


@api_view(["DELETE"])
def delete_brand(request : Request, brand_id):
    
    try:
        brand = Brand.objects.get(id=brand_id)
    except:
        res_data = {
            "msg":"Fail to found brand, please check provided id."
        }

        return Response(res_data) 

    brand.delete()

    res_data = {
            "msg":f"Brand {brand.title} deleted Successfully!"
        }
    
    return Response(res_data)




# Product CRUD

@api_view(['POST'])
def create_product(request : Request):
    
    product_ser = ProductSerializer(data=request.data)
    

    if product_ser.is_valid():
        product_ser.save()
    else:
        return Response({"msg" : "Product couldn't be created.", "errors" : ProductSerializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Product created Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def list_products(request : Request):
    
    if "skip" in request.query_params and "get" in request.query_params:
        skip = int(request.query_params.get("skip", 0))
        get = int(request.query_params.get("get", 10))


        product = Product.objects.all()[skip:get]
        product_data = ProductSerializer(instance=product, many=True).data
    else:
        product = Product.objects.all()
        product_data = ProductSerializer(instance=product, many=True).data

    
    if "brand" in request.query_params:
        search_phrase = request.query_params["brand"]
        product = Product.objects.filter(brand=search_phrase)
        product_data = ProductSerializer(instance=product, many=True).data

    
    return Response({"msg" : "list of all products", "products" : product_data})

@api_view(['GET'])
def list_products_of_brand(request : Request, brand_name):
    
    try:
        brand = Brand.objects.get(title=brand_name)
        product = Product.objects.filter(brand=brand.id)
        product_data = ProductSerializer(instance=product, many=True).data

        return Response({"msg" : "list of all products", "products" : product_data})
    except:
         return Response({"msg" : "Product not found !!"})

@api_view(['PUT'])
def update_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
    except:
        return Response({"msg" : "Product couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
    
    product_serializer = ProductSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "Product couldn't be updated", "errors" : product_serializer.errors})

    return Response({"msg" : "Product updated Successfully!"})


@api_view(["DELETE"])
def delete_product(request : Request, product_id):
    
    try:
        product = Product.objects.get(id=product_id)
    except:
        res_data = {
            "msg":"Fail to found Product, please check provided id."
        }

        return Response(res_data) 

    product.delete()

    res_data = {
            "msg":f"Product {product.name} deleted Successfully!"
        }
    
    return Response(res_data)