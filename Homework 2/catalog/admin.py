from django.contrib import admin
from catalog.models import Category, Product, Version, BlogPost


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category",)
    search_fields = ("name", "description")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "number", "name", "is_active")
    list_filter = ("product", "is_active")
    search_fields = ("name",)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "views_count", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "content", "views_count", "is_published")
