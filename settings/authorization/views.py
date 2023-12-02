from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.views.generic.edit import CreateView

from authorization.models import Cart, BookInCart
from books.models import Book


# Create your views here.
class YourView(LoginRequiredMixin, CreateView):
    login_url = '/authorization/login/'


class LoginView(auth_views.LoginView):
    template_name = "authorization/login.html"


class LogoutView(auth_views.LogoutView):
    next_page = 'homepage'


class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("authorization:login")
    template_name = "authorization/signup.html"


class AddToCartView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.get(user=user)
        book_pk = kwargs.get("pk")
        book = Book.objects.get(pk=book_pk)
        if cart.check_if_book_already_in_cart(book):
            return redirect(to=reverse("books:view-book", kwargs={
                "pk": book_pk
            }))
        book_in_cart = BookInCart.objects.create(
            book=book,
            count=1,
        )
        cart.books.add(book_in_cart)
        return redirect(to=reverse("books:view-book", kwargs={
            "pk": book_pk
        }))
