from rest_framework import serializers
from sale.models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class ProductOfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOfUser
        fields = "__all__"

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
