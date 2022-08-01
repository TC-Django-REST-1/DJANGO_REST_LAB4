from hashlib import new
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from rest_framework import status

from .models import Brand, Product
from .serializers import ProductSerializer


@api_view(["POST"])
def add_brand(request : Request):

    title = request.data["title"]
    description = request.data["description"]
    established_at = request.data["established_at"]
    city = request.data["city"]

    new_brand = Brand(title=title, description=description, established_at=established_at, city=city)
    new_brand.save()

    res_data = {
        "msg" : "Created Brand Successfully"
    }

    return Response(res_data)


@api_view(["GET"])
def list_brands(request : Request):
    all_brands=Brand.objects.all()
    all_brands_list = [{"id" : brand.id, "title" : brand.title, "description": brand.description, "city": brand.city} for brand in all_brands]
    
    res_data = {
        "msg" : "A list of All Brands",
        "books" : all_brands_list
    }
    return Response(res_data, status=status.HTTP_200_OK)



@api_view(['PUT'])
def update_brand(request : Request, brand_id):

    brand=Brand.objects.get(id=brand_id)

    brand.title = request.data["title"]
    brand.description = request.data["description"]
    brand.established_at = request.data["established_at"]
    brand.city = request.data["city"]
    brand.save()

    return Response({"msg" : "Your brand is updated !"})



@api_view(["DELETE"])
def delete_brand(request : Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response({"msg" : "The brand is not Found!"})

    return Response({"msg" : f"delete the following brand {brand.title}"})



@api_view(['POST'])
def add_product(request : Request):

    product_serializer = ProductSerializer(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({"msg" : "couldn't create a product", "errors" : product_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({"msg" : "Product Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_products(request : Request):

    products = Product.objects.all()
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

    return Response({"msg" : "Product updated successfully"})



@api_view(["DELETE"])
def delete_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({"msg" : "The product is not Found!"})

    return Response({"msg" : f"delete the following product {product.name}"})



@api_view(['GET'])
def get_product(request : Request, product_id):

    try:
        product = Product.objects.get(id=product_id)
        product_serializer = ProductSerializer(instance=product, data=request.data)
        return Response({"msg" : "Product updated successfully", "product": product_serializer})
    except Exception as e:
        return Response({"msg" : "This product is not found"}, status=status.HTTP_404_NOT_FOUND)




