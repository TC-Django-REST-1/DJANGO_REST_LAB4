from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Brand, Product
from .serializers import CommentSerializer
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def list_brands(request :Request):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    brands = Brand.objects.all()
    brands_data = CommentSerializer(instance=brands, many=True).data[skip:get]

    

    return Response({"msg" : "list of all Brand", "Brands" : brands_data})


@api_view(['POST'])
def add_brand(request : Request):
    
    brand_serializer = CommentSerializer(data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "couldn't create a brand", "errors" : brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({"msg" : "Brand Added Successfully!"}, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def update_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg" : "This brand is not found"}, status=status.HTTP_404_NOT_FOUND)

    brand_serializer = CommentSerializer(instance=brand, data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : brand_serializer.errors})

    return Response({"msg" : "Brand updated successfully"})


@api_view(["DELETE"])
def delete_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : "The Brand is not Found!"})

    return Response({"msg" : f"delete the following Brand {brand.title}"})

@api_view(['GET'])
def search_brands(request :Request):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_brand = Brand.objects.filter(title__startswith=search_phrase)[skip:get]
    else:
        return Response({"msg" : "please enter the brand name"})

    all_brand_list = [{"id" : brand.id, "title" : brand.title, "description" : brand.description, "established_at" : brand.established_at, "city":brand.city,} for brand in all_brand]

    return Response({"msg" :{"here all brands"}, "brands": all_brand_list})
    

# Product 

@api_view(['GET'])
def list_product(request :Request, product_id):
    
    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    try:
        brand = Brand.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg" : "The Brand is not Found!"})


    product = Product.objects.all()
    product_data = CommentSerializer(instance=product, many=True).data[skip:get]

    return Response({"msg" : "list of all Brand", "Brands" : product_data})


@api_view(['POST'])
def add_product(request : Request):

    product_serializer = CommentSerializer(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't create a product", "errors" : product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

    return Response({"msg" : "Product Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['PUT'])
def update_product(request : Request, product_id):
    
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return Response({"msg" : "This product is not found"}, status=status.HTTP_404_NOT_FOUND)

    product_serializer = CommentSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" : product_serializer.errors})

    return Response({"msg" : "Product updated successfully"})


@api_view(["DELETE"])
def delete_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({"msg" : "The Brand is not Found!"})

    return Response({"msg" : f"delete the following product {product.name}"})


@api_view(['GET'])
def list_products_of_brand(request :Request, brand_id):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({"msg" : "This brand is not found!!"}, status=status.HTTP_404_NOT_FOUND)

    products_of_brand = Product.objects.filter(brand=brand)[skip:get]

    return Response({"msg" : f"all the following product of {brand.title}", "products": products_of_brand})