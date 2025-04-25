from rest_framework import serializers
from .models import Kitchen, Category, SubCategory, Product, Comment, Rating , UserProfile , Order


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

    class Meta:
        model = SubCategory
        fields = ["id", "name", "slug", "category"]



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





