from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from user import serializers
from cart.serializers import CheckOutSerializer
from cart.models import CheckOut
from user.permissions import IsAdmin
from book.models import Book

# Create your views here.

class CreateCheckout(generics.CreateAPIView):
    permission_classes = (IsAdmin,)
    
    def get_serializer_class(self):
        return CheckOutSerializer
    
    def create(self, request, *args, **kwargs):
        serializer=CheckOutSerializer(data=request.data)

        try:
            book=Book.objects.get(id=request.data.get('book'))
            requiredQuantity=request.data.get('quantity')

            if not book.is_available:
                return Response("Book not available")
            if requiredQuantity>book.quantity:
                return Response("Not enough book available")
            elif serializer.is_valid():
                book.quantity-=requiredQuantity
                book.save()
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response("Book does not exist")

class ListCheckouts(generics.ListAPIView):
    permission_classes = (IsAdmin,)
    serializer_class=CheckOutSerializer
    queryset=CheckOut.objects.all()

class ListCheckout(generics.RetrieveAPIView):
    permission_classes = (IsAdmin,)
    serializer_class=CheckOutSerializer
    queryset=CheckOut.objects.all()

class UpdateCheckoutDetails(generics.UpdateAPIView):
    permission_classes = (IsAdmin,)
    def get_serializer_class(self):
        return CheckOutSerializer
    
    def update(self, request, *args, **kwargs):
        try:
            book=Book.objects.get(id=request.data.get('book'))
            instance=CheckOut.objects.get(id=kwargs.get('pk'))
            serializer=CheckOutSerializer(data=request.data,instance=instance)
            requiredQuantity=request.data.get('quantity')
            if not book.is_available and requiredQuantity>instance.quantity:
                return Response("Book not available")
            if requiredQuantity>book.quantity+instance.quantity:
                return Response("Not enough Books Available")
            
            elif serializer.is_valid():
                if requiredQuantity>instance.quantity:
                    book.quantity-=requiredQuantity-instance.quantity
                    book.save()
                
                elif requiredQuantity<instance.quantity:
                    book.quantity+=instance.quantity-requiredQuantity
                    book.save()
                
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        except:
            return Response("Book does not exist")

class DeleteCheckout(generics.DestroyAPIView):
    permission_classes = (IsAdmin,)
    queryset = CheckOut.objects.all()

    def delete(self, request, *args, **kwargs):
        try:
            book = Book.objects.get(id = request.data.get('book'))
            instance = CheckOut.objects.get(id=kwargs.get('pk'))
            book.quantity+=instance.quantity
            book.save()
            instance.delete()
            return Response('Book Deleted')
        except:
            return Response('Book does not exist')