from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (KitchenViewSet,CategoryViewSet,SubCategoryViewSet,ProductViewSet,
    CommentViewSet,RatingViewSet,KitchenAdminProfileViewSet , CourierProfileViewSet)

router = DefaultRouter()
router.register(r"kitchens", KitchenViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"subcategories", SubCategoryViewSet)
router.register(r"products", ProductViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"ratings", RatingViewSet)
router.register(r"kitchen-admins", KitchenAdminProfileViewSet)
router.register(r"couriers", CourierProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]