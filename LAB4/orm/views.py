from turtle import title
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer
from rest_framework import status

# Create your views here.

                       # ------------------- CRUD Process For Brand ----------------------- #

# ----------------------- Add Brand ---------------------------#

@api_view(['POST'])
def add_brand(request : Request):
    
    brand_serializer = BrandSerializer(data=request.data)

    if brand_serializer.is_valid():
        brand_serializer.save()
    else:
        return Response({'msg' : 'could not add a brand', 'errors': brand_serializer.errors}, status=status.HTTP_403_FORBIDDEN)
    

    return Response({'msg' : 'brand added successfully!'}, status=status.HTTP_201_CREATED)

# ---------------------------- List All Brands ------------------- #

@api_view(['GET'])
def list_brand(request: Request):

    skip = int(request.query_params.get('skip',0))
    get = int(request.query_params.get('get', 3))
    
    brands = Brand.objects.all()
    brands_list = BrandSerializer(instance=brands, many=True).data[skip:get] #.data to convert object of serializer to json obj.
    
    return Response({'msg' : 'List of all brands!', 'brands' : brands_list})

# ------------------------ Update a Brand ---------------------- #

@api_view(['PUT'])
def update_brand(request: Request, brand_id):

    try:
        brand = Brand.objects.get(id=brand_id)
    except Exception as e:
        return Response({'msg' : 'brand not found'}, status=status.HTTP_404_NOT_FOUND)

    brand_updated = BrandSerializer(instance=brand, data=request.data)

    if brand_updated.is_valid():
        brand_updated.save()
    else:
        return Response({'msg' : 'could not update a brand!', 'errors': BrandSerializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({'msg' : 'a brand updated successfully!'}, status=status.HTTP_202_ACCEPTED)

# ---------------------------- Delete a Brand ------------------- #

@api_view(['DELETE'])
def remove_brand(request: Request, brand_id):
    
    try:
        brand = Brand.objects.get(id=brand_id)
        brand.delete()
    except Exception as e:
        return Response({'msg' : 'could not find a brand!'}, status=status.HTTP_404_NOT_FOUND)

    
    return Response({'msg' : 'brand deleted successfully!'}, status=status.HTTP_302_FOUND)

@api_view(['GET'])
def search_brand(request: Request):
    
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        brand = Brand.objects.filter(title__contains=search_phrase).all()
        
    else:
        return Response({'msg' : 'No brand found!'})

    brand_found = BrandSerializer(instance=brand, many=True).data
    
    return Response({'msg': 'Brand found!', 'brand' : brand_found})




                         #--------------------------- CRUD Process For Product ----------------- #

# ---------------------------- Add Product --------------------------- #

@api_view(['POST'])
def add_product(request: Request):
    
    product_serializer = ProductSerializer(data=request.data)

    if product_serializer.is_valid():
        product_serializer.save()
    else:
        return Response({'msg' : 'could not add a product', 'errors': ProductSerializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({'msg': 'product added successfully!'}, status=status.HTTP_201_CREATED)

# ------------------------------ List All Products ------------------------ #

@api_view(['GET'])
def list_product(request: Request):

    skip = int(request.query_params.get('skip',0))
    get = int(request.query_params.get('get', 3))
    
    products = Product.objects.all()
    product_list = ProductSerializer(instance=products, many=True).data[skip:get] #.data to convert list of Serializer obj to JSON obj

    return Response({'msg' : 'List of products', 'products': product_list}, status=status.HTTP_200_OK)

# --------------------------- Update a Product -------------------------- #

@api_view(['PUT'])
def update_product(request: Request, product_id):
    
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return Response({'msg' : 'could not find a product1'}, status=status.HTTP_404_NOT_FOUND)
    
    product_updated = ProductSerializer(instance=product, data=request.data)

    if product_updated.is_valid():
        product_updated.save()
    else:
        return Response({'msg' : 'could not update a product!', 'errors' : ProductSerializer.errors}, status=status.HTTP_403_FORBIDDEN)
    
    return Response({'msg' : 'product updated successfully!'}, status=status.HTTP_202_ACCEPTED)


# -------------------------- Delete a product ----------------------- #

@api_view(['DELETE'])
def delete_product(request: Request, product_id):
    
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
    except Exception as e:
        return Response({'msg' : 'could not find a product'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response({'msg' : 'product deleted successfull!'}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def list_products_of_brand(request: Request):

    if 'search' in request.query_params:
        search_id = int(request.query_params.get('search'))
        all_products = Product.objects.filter(brand_id=search_id)
    else:
        return Response({'msg' : 'No products found for this brand!'})# This doesn't appear when there are no products in a given brand
    
    products = ProductSerializer(instance=all_products, many=True).data

    return Response({'msg': 'list products of specific brand', 'products': products})



