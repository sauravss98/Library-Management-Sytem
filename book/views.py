from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.permissions import IsAdmin
from book.models import Book
from book.serializers import BookSerializer

class CreateBookDetails(generics.CreateAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = BookSerializer

class ListBooks(generics.ListAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class ListBook(generics.RetrieveAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class UpdateBookDetails(generics.UpdateAPIView):
    permission_classes = (IsAdmin,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class DeleteBook(generics.DestroyAPIView):
    permission_classes = (IsAdmin,)
    queryset = Book.objects.all()