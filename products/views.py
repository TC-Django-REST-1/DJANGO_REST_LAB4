from typing import Any, Callable
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from .models import Brands as BrandsModel, Products as ProductsModel
from .serializers import BrandsSerializer, ProductsSerializer


def get_query(value: Any, default: Any, condition: Callable, func: Callable) -> Any:
    return func(value) if condition(value) else default


class Brands(APIView):
    def get(self, request: Request) -> Response:
        """List brands"""
        skip = get_query(request.query_params.get("skip", ""), None, str.isdigit, int)
        to = get_query(request.query_params.get("to", "10"), 10, str.isdigit, int)
        name = request.query_params.get("name", "")
        serializer = BrandsSerializer(
            instance=BrandsModel.objects.filter(name__icontains=name).all()[skip:to],
            many=True,
        )
        return Response({"data": serializer.data})

    def post(self, request: Request) -> Response:
        """Post new brand to databases"""
        serializer = BrandsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"msg": "Cannot serializer data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class Brand(APIView):
    def get(self, _request: Request, pk: int) -> Response:
        """Returns brand by id"""
        try:
            return Response(BrandsSerializer(BrandsModel.objects.get(pk=pk)).data)
        except ObjectDoesNotExist:
            return Response(
                {"msg": f"There is no brand with '{pk}' id"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request: Request, pk: int) -> Response:
        """Update existing brand"""
        try:
            serializer = BrandsSerializer(
                BrandsModel.objects.get(pk=pk), data=request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                {"msg": "Cannot serializer data", "errors": serializer.errors},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ObjectDoesNotExist:
            return Response(
                {"msg": f"There is no brand with '{pk}' id"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, _request: Request, pk: int) -> Response:
        """Returns brand by id"""
        try:
            brand = BrandsModel.objects.get(pk=pk)
            brand.delete()
            return Response(
                {"msg": f"'{brand.name}' deleted successfully"},
                status=status.HTTP_202_ACCEPTED,
            )
        except ObjectDoesNotExist:
            return Response(
                {"msg": f"There is no brand with '{pk}' id"},
                status=status.HTTP_404_NOT_FOUND,
            )


class Products(APIView):
    def get(self, request: Request) -> Response:
        """List products"""
        skip = get_query(request.query_params.get("skip", ""), None, str.isdigit, int)
        to = get_query(request.query_params.get("to", "10"), 10, str.isdigit, int)
        name = request.query_params.get("name", "")
        brand = request.query_params.get("brand", "")
        serializer = ProductsSerializer(
            instance=ProductsModel.objects.filter(name__icontains=name, brand__name__icontains=brand).all()[skip:to],
            many=True,
        )
        return Response({"data": serializer.data})

    def post(self, request: Request) -> Response:
        """Post new product to databases"""
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {"msg": "Cannot serializer data", "errors": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )


class Product(APIView):
    def get(self, _request: Request, pk: int) -> Response:
        """Returns product by id"""
        try:
            return Response(ProductsSerializer(ProductsModel.objects.get(pk=pk)).data)
        except ObjectDoesNotExist:
            return Response(
                {"msg": f"There is no product with '{pk}' id"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def put(self, request: Request, pk: int) -> Response:
        """Update existing product"""
        try:
            serializer = ProductsSerializer(
                ProductsModel.objects.get(pk=pk), data=request.data
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                {"msg": "Cannot serializer data", "errors": serializer.errors},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ObjectDoesNotExist:
            return Response(
                {"msg": f"There is no product with '{pk}' id"},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, _request: Request, pk: int) -> Response:
        """Returns product by id"""
        try:
            product = ProductsModel.objects.get(pk=pk)
            product.delete()
            return Response(
                {"msg": f"'{product.name}' deleted successfully"},
                status=status.HTTP_202_ACCEPTED,
            )
        except ObjectDoesNotExist:
            return Response(
                {"msg": f"There is no product with '{pk}' id"},
                status=status.HTTP_404_NOT_FOUND,
            )
