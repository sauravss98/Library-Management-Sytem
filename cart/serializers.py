from rest_framework import serializers
from cart.models import CheckOut


class CheckOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = ('id','student','book','quantity','created_at','updated_at')
        read_only_fields = ['created_at','updated_at']
