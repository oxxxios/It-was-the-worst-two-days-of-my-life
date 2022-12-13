from rest_framework import serializers
from products.models import Product, Category, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "category_name is_popular".split()

class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = "text rate author".split()

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "title price image subtext".split()

class ProductDetailSerializer(serializers.ModelSerializer):
    product = CategorySerializer(many=False)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = "__all__"