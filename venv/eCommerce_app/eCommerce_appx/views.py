
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import eCommerce_app, Product
from .serializers import eCommerce_appxerializer, ProductSerializer



@api_view(['POST'])
def add_eCommerce_appx(request : Request):
    
    eCommerce_appxerializer = eCommerce_appxerializer(data=request.data)

    if eCommerce_app_serializeris_valid():
        eCommerce_app_serializer.save()
    else:
        return Response({"msg" : "couldn't create aeCommerce_app", "errors" : eCommerce_app_serializer.errors}, status=status.HTTP_403_FORBIDDEN)


    return Response({"msg" : "eCommerce_appx Added Successfully!"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def list_eCommerce_appxs(request : Request):

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        eCommerce_app =eCommerce_app.objects.filter(title=search_phrase)[skip:get]
    else:
       eCommerce_app =eCommerce_app.objects.all()

   eCommerce_app_data =eCommerce_appxerializer(instance=eCommerce_app, many=True).data
   return Response({"msg" : "list of all eCommerce_appx", "eCommerce_appxs" :eCommerce_app_data})
    
@api_view(['PUT'])

def update_eCommerce_appx(request : Request,eCommerce_app_id):

    try:
       eCommerce_appx =eCommerce_app.objects.get(id=eCommerce_app_id)
    except Exception as e:
        return Response({"msg" : "ThiseCommerce_app is not found"}, status=status.HTTP_404_NOT_FOUND)

   eCommerce_appxerializer = eCommerce_appxerializer(instance=eCommerce_appx, data=request.data)

    if eCommerce_app_serializer.is_valid():

       eCommerce_app_serializer.save()
    else:
        return Response({"msg" : "couldn't update", "errors" :eCommerce_app_serializer.errors})

    return Response({"msg" : "eCommerce_appx updated successfully"})


@api_view(["DELETE"])
def delete_eCommerce_appx(request : Request,eCommerce_app_id):

    try:
       eCommerce_appx =eCommerce_app.objects.get(id=eCommerce_appx_id)
       eCommerce_appx.delete()
    except Exception as e:
        return Response({"msg" : "TheeCommerce_app is not Found!"})

    return Response({"msg" : f"delete the followingeCommerce_app {eCommerce_appxs.title}"})




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

    return Response({"msg" : "list of all products", "eCommerce_appxs" : products_data})




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
        return Response({"msg" : "TheeCommerce_app is not Found!"})

    return Response({"msg" : f"delete the followingeCommerce_app {product.eCommerce_appx}"})
