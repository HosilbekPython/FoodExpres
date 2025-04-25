from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models import Avg


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=355)
    created_at = models.DateTimeField(auto_now_add=True)
    all_orders = models.JSONField(default=list, blank=True)  # JSONField sifatida qoldirildi

    def __str__(self):
        return f"Profile of {self.user.username}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"


# Boshqa modellar (Kitchen, Category, SubCategory) o'zgarmagan holda qoladi
class Kitchen(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kitchen"
        verbose_name_plural = "Kitchens"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"
        unique_together = ["name", "category"]


class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.TextField()
    kitchen = models.ForeignKey(Kitchen, on_delete=models.CASCADE, related_name="products")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="product/image/")
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Chegirma foizda
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def rating(self):
        # Barcha reytinglarning o'rtacha qiymatini hisoblash
        avg_rating = self.ratings.aggregate(Avg("score"))["score__avg"]
        return round(avg_rating, 2) if avg_rating else 0.0

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="ratings")  # User o‘rniga UserProfile
    score = models.PositiveIntegerField(choices=((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating {self.score} by {self.user.user.username} on {self.product.title}"

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"
        unique_together = ["user", "product"]


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="comments")  # User o‘rniga UserProfile
    text = models.TextField()
    rating = models.ForeignKey(
        Rating, on_delete=models.SET_NULL, null=True, blank=True, related_name="comment"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.user.username} on {self.product.title}"

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


class Order(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="orders")  # User o‘rniga UserProfile
    products = models.ManyToManyField(Product, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order by {self.user.user.username} at {self.created_at}"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"