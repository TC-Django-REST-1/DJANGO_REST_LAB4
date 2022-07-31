from operator import is_
from turtle import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.db.models.functions import Lower
from rest_framework import status

from .models import Brand, Product
from .serializers import ProductSerializer, BrandSerializer


@api_view(["POST"])
def add_brand(request: Request):

    new_brand = BrandSerializer(data=request.data)
    if new_brand.is_valid():
        new_brand.save()
    else:
        print(request.data["title"])
        return Response({
            "msg": new_brand.errors, "details": (new_brand.data.values())
        }, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({
        "msg": f"create a new brand with title {{ {new_brand.data.get('title')} }} Successfully"
    }, status=status.HTTP_200_OK)


@api_view(["GET"])
def list_brand(request: Request):

    # returns the total count of Brand in the database, for testing only
    print(Brand.objects.count())
    all_brands = Brand.objects.order_by(Lower("title"))

    skip = int(request.query_params.get("skip", 0))
    get = int(request.query_params.get("get", 10))

    if "search" in request.query_params:
        search_phrase = request.query_params["search"]
        all_brands = Brand.objects.filter(
            title__contains=search_phrase).values()
    else:
        all_brands = Brand.objects.order_by(Lower("title"))

    res_data = {
        "msg": "A list of All brands",
        "brands": all_brands[skip:get]
    }

    return Response(res_data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_brand(request: Request, brand_title: str):

    data_obj = Brand.objects.get(title=brand_title)
    data= BrandSerializer(data_obj,request.data)
    if data.is_valid():
        print(data)
        data.save()
        return Response({"msg": "Your book is updated !"})
    else:
        print(data.errors)
        return Response({"msg": data.errors})


@api_view(["DELETE"])
def delete_brand(request: Request, brand_title):

    try:
        brand = Brand.objects.get(title=brand_title)
        brand.delete()
    except Exception as e:
        return Response({"msg": f"The brand {brand_title} is not Found!"})

    return Response({"msg": f"delete the following brand {brand_title}"})


# @api_view(['POST'])
# def add_comment(request: Request):

#     comment_serializer = CommentSerializer(data=request.data)

#     if comment_serializer.is_valid():
#         comment_serializer.save()
#     else:
#         return Response({"msg": "couldn't create a comment", "errors": comment_serializer.errors}, status=status.HTTP_403_FORBIDDEN)

#     return Response({"msg": "Comment Added Successfully!"}, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# def list_comments(request: Request):

#     comments = Comment.objects.all()
#     comments_data = CommentSerializer(instance=comments, many=True).data

#     return Response({"msg": "list of all comments", "comments": comments_data})


# @api_view(['PUT'])
# def update_comment(request: Request, comment_id):

#     try:
#         comment = Comment.objects.get(id=comment_id)
#     except Exception as e:
#         return Response({"msg": "This comment is not found"}, status=status.HTTP_404_NOT_FOUND)

#     comment_serializer = CommentSerializer(instance=comment, data=request.data)

#     if comment_serializer.is_valid():
#         comment_serializer.save()
#     else:
#         return Response({"msg": "couldn't update", "errors": comment_serializer.errors})

#     return Response({"msg": "Comment updated successfully"})
