from django.db import models
from django.contrib.auth import get_user_model

from books.models import Book

# Create your models here.

User = get_user_model()


class BookInCart(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)


class Cart(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, unique=True)
    books = models.ManyToManyField(to=BookInCart, blank=True)

    def check_if_book_already_in_cart(self, book_to_check):
        for book_in_cart in self.books.all():
            book = book_in_cart.book
            if book == book_to_check:
                return True

    def get_total_price(self):
        total_price = 0
        for book_in_cart in self.books.all():
            count = book_in_cart.count
            price = book_in_cart.book.book_price
            total_price += price * count
        return total_price
