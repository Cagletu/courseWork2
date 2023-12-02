from django.shortcuts import render
from django.views import generic


# Create your views here.


# Homepage
from books import models


class HomePage(generic.ListView):
    model = models.Book
    template_name = "home-page/home_page.html"
