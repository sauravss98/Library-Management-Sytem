from dataclasses import field
import email
from multiprocessing.managers import Token
from pyexpat import model
from turtle import mode
from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','idNumber','password')
        extra_kwargs={'password':{'write_only':True}}

    # def create(self, validated_data):
    #     user=User.objects.create_user(**validated_data)
    #     return user
    def create(self, validated_data):
        user = User(
            idNumber=validated_data['idNumber'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user





