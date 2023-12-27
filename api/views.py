from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
 
from ecommerce.models import ProductModel
from .serializer import ApiSerializer

class ProductAPIView(APIView):
    """Lists all products, or creates a new one"""

    def get(self, request, format=None): 
        products = ProductModel.objects.all()
        serializer = ApiSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):
    """Allows to 'GET' 'UPDATE' or 'DELETE' an specific product"""

    def get_object_pk(self, pk):
        "gets a ProductModel instance pk"
        try:
            return ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        product = self.get_object_pk(pk)
        serializer = ApiSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        product = self.get_object_pk(pk)
        serializer = ApiSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = self.get_object_pk(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#ViewSet
class ProductApiViewSet(ViewSet):
    """API ViewSet"""

    def list(self, request, format=None):
        """Enlists the products stored in the DB""" 
        products = ProductModel.objects.all()
        serializer = ApiSerializer(products, many=True)
        return Response(serializer.data)
    
    def create(self, request, format=None):
        """Creates a new product(instance) and stores it in the DB"""
        serializer = ApiSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_object_pk(self, pk):
        "gets a ProductModel instance pk"
        try:
            return ProductModel.objects.get(pk=pk)
        except ProductModel.DoesNotExist:
            raise Http404
        
    def retrieve(self, request, pk, format=None):
        """Gets a single product base on its ID"""
        product = self.get_object_pk(pk)
        serializer = ApiSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk, format=None):
        """Updates a single product from the DB"""
        product = self.get_object_pk(pk)
        serializer = ApiSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk, format=None):
        """Deletes a simgle product from the DB"""
        product = self.get_object_pk(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)