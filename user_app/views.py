from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend
from .models import Kitchen, Category, SubCategory, Product, Comment, Rating , CourierProfile , KitchenAdminProfile
from .serializers import (KitchenSerializer,CategorySerializer,SubCategorySerializer,
    ProductSerializer,CommentSerializer,RatingSerializer,KitchenAdminProfileSerializer,
    CourierProfileSerializer )


class KitchenViewSet(viewsets.ModelViewSet):
    queryset = Kitchen.objects.all()
    serializer_class = KitchenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["category"]
    search_fields = ["name"]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["kitchen", "category", "subcategory"]  # brand olib tashlandi
    search_fields = ["title", "description"]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        rating_score = self.request.data.get("rating_score")
        product_id = self.request.data.get("product")
        user = self.request.user

        if rating_score:
            rating, created = Rating.objects.get_or_create(
                user=user,
                product_id=product_id,
                defaults={"score": rating_score},
            )
            if not created:
                rating.score = rating_score
                rating.save()
        else:
            rating = None

        serializer.save(user=user, rating=rating)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class KitchenAdminProfileViewSet(viewsets.ModelViewSet):
    queryset = KitchenAdminProfile.objects.all()
    serializer_class = KitchenAdminProfileSerializer

class CourierProfileViewSet(viewsets.ModelViewSet):
    queryset = CourierProfile.objects.all()
    serializer_class = CourierProfileSerializer




