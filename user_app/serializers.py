from rest_framework import serializers
from django.utils.text import slugify

from .models import (Kitchen, Category, SubCategory, Product, Comment, Rating , UserProfile
                    , Order , KitchenAdminProfile , CourierProfile , User)


class KitchenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitchen
        fields = ["id", "name", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug', 'category', 'category_id', 'created_at', 'updated_at']
        read_only_fields = ['id', 'slug', 'category', 'created_at', 'updated_at']

    def validate(self, data):
        if not data.get('category_id'):
            raise serializers.ValidationError("category_id is required.")
        return data

    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise serializers.ValidationError(f"Category with id {category_id} does not exist.")

        sub_category = SubCategory.objects.create(
            category=category,
            **validated_data
        )
        return sub_category

    def update(self, instance, validated_data):
        category_id = validated_data.pop('category_id', None)
        if category_id:
            try:
                category = Category.objects.get(id=category_id)
                instance.category = category
            except Category.DoesNotExist:
                raise serializers.ValidationError(f"Category with id {category_id} does not exist.")

        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, source="user.user.username")  # UserProfile orqali username
    product = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = ["id", "product", "user", "score", "created_at"]


class ProductSerializer(serializers.ModelSerializer):
    kitchen = KitchenSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    subcategory = SubCategorySerializer(read_only=True)
    discounted_price = serializers.SerializerMethodField()
    rating = serializers.ReadOnlyField()  # Rating faqat o'qish uchun
    photo = serializers.ImageField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "kitchen",
            "category",
            "subcategory",
            "price",
            "photo" ,
            "discount",
            "discounted_price",
            "rating",
            "created_at",
            "updated_at",
        ]

    def get_discounted_price(self, obj):
        return obj.price * (1 - obj.discount / 100)



class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, source="user.user.username")  # UserProfile orqali username
    product = serializers.StringRelatedField(read_only=True)
    rating = RatingSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "product", "user", "text", "rating", "created_at", "updated_at"]


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, source="user.user.username")  # UserProfile orqali username
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "products", "created_at"]




class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "address",
            "phone_number",
            "location",
            "created_at",
            "orders",
            "all_orders",
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class KitchenAdminProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    kitchen = KitchenSerializer(read_only=True)

    class Meta:
        model = KitchenAdminProfile
        fields = ['id', 'user', 'phone_number', 'kitchen', 'created_at']
        read_only_fields = ['created_at']

class CourierProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CourierProfile
        fields = ['id', 'user', 'phone_number', 'photo', 'passport_series', 'passport_number', 'created_at']
        read_only_fields = ['created_at']




