from django.contrib import admin
from .models import (Kitchen, Category, SubCategory, Product, Comment, Rating, Order,
                     UserProfile , KitchenAdminProfile , CourierProfile , User)


@admin.register(Kitchen)
class KitchenAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    search_fields = ["name"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "slug", "created_at"]
    search_fields = ["name", "category__name"]
    list_filter = ["category"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "kitchen", "category", "subcategory", "price", "discount", "rating", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["kitchen", "category", "subcategory"]
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ["rating"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "rating", "created_at"]
    search_fields = ["text", "user__username", "product__title"]
    list_filter = ["product", "user"]


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ["product", "user", "score", "created_at"]
    search_fields = ["user__username", "product__title"]
    list_filter = ["product", "user"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "created_at"]  # total_price va status olib tashlandi
    search_fields = ["user__username", "id"]
    list_filter = ["created_at"]  # status olib tashlandi
    readonly_fields = ["created_at"]  # updated_at olib tashlandi


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "address", "location", "created_at"]
    search_fields = ["user__username", "phone_number", "address", "location"]
    list_filter = ["created_at"]
    readonly_fields = ["created_at"]


@admin.register(KitchenAdminProfile)
class KitchenAdminProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "kitchen", "created_at"]
    search_fields = ["user__username", "phone_number", "kitchen__name"]
    list_filter = ["created_at"]
    readonly_fields = ["created_at"]


@admin.register(CourierProfile)
class CourierProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "phone_number", "passport_series", "passport_number", "created_at"]
    search_fields = ["user__username", "phone_number", "passport_series", "passport_number"]
    list_filter = ["created_at"]
    readonly_fields = ["created_at"]






