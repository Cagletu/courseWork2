from django.contrib import admin

from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'counter_book', 'active')
    fieldsets = (
        ('Main info about book', {
            'fields': (
                'book_name',
                'book_image',
                'book_price',
                'autor',
                'series',
                'genre',
                'ISBN',
                'publishing_house',
                'counter_book',
                'active',
            )
        }),
        ('Advanced info about book', {
            'fields': (
                'year_publishing',
                'page',
                'binding',
                'format_book',
                'description',
                'weight',
                'age_restrictions',
            )
        }),
    )


# todo: Добавить лист дисплей и филдсеты, для данных моделей
admin.site.register(models.Series)
admin.site.register(models.Genre)
admin.site.register(models.PublishingHouse)


@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('autor_name',)
    fieldsets = (
        ('Info about author', {
            'fields': ('autor_name',)
        }),
        (None, {
            'fields': ('autor_description',)
        }),
    )
