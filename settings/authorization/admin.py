from django.contrib import admin

# Register your models here.

from .models import Cart, BookInCart

admin.site.register(BookInCart)


# class BookInCartInline(admin.TabularInline):
#     model = BookInCart

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "get_total_price"
    )
    # inlines = (
    #     BookInCartInline,
    # )
