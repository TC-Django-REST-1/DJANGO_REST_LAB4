from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .serializers import BrandSerializer
from .serializers import ProductSerializer
from .models import Brand
from .models import Product

# Brand Section

@api_view(['POST'])
def create_brand(request : Request):

    brand_serializer = BrandSerializer(data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "couldn't create a brand", "errors" : brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "brand Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_brand(request : Request):
    brands = Brand.objects.all()

    skip = int(request.query_params.get("skip"))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        brands = Brand.objects.filter(title__startswith=search_phrase)[skip:get]
    else:
        brands = Brand.objects.all().order_by('established_at')[skip:get]
        
    brands_data = BrandSerializer(instance=brands, many=True).data

    return Response({"msg" : "list of all brands", "brands" : brands_data})


@api_view(['PUT'])
def update_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg" : "This brand is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    brand_serializer = BrandSerializer(instance=brand, data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : brand_serializer.errors})

    return Response({"msg" : "Brand updated successfully"})


@api_view(['DELETE'])
def delete_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : "This Brand is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "Brand Deleted successfully"})


@api_view(['GET'])
def get_brandName(request : Request, brand_name):

    try:
        brand = Brand.objects.get(title=brand_name)
    except Exception as e:
        return Response({"msg" : "This brand is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    rands_data = BrandSerializer(instance=brand).data
    return Response({"msg" : f"list of all brands Named {brand_name}", "brands" : rands_data})


    # Product Section

@api_view(['POST'])
def create_product(request : Request):

    product_serializer = ProductSerializer(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't create a product", "errors" : product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    
    return Response({"msg" : "product Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_product(request : Request):

    products = Product.objects.all()

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        products = Product.objects.filter(name__startswith=search_phrase)[skip:get]
    else:
        products = Product.objects.all().order_by('-price')[skip:get]

    products_data = ProductSerializer(instance=products, many=True).data

    return Response({"msg" : "list of all products", "products" : products_data})


@api_view(['PUT'])
def update_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg" : "This product is not found"}, status=status.HTTP_404_NOT_FOUND)
    
    product_serializer = ProductSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : product_serializer.errors})

    return Response({"msg" : "product updated successfully"})


@api_view(['DELETE'])
def delete_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({"msg" : "This product is not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response({"msg" : "product Deleted successfully"})
