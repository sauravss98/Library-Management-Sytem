from rest_framework import serializers
from book.models import Book

class BookSerializer(serializers.ModelSerializer):
    is_available = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ('id', 'title','authorName','quantity', 'is_available')
    
    def get_is_available(self, instance):
        if instance.is_available:
            return "Available"
        else:
            return "Not Available"
