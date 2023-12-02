from django.shortcuts import render
from django.views import generic

from . import models


# Create your views here.
# Autor
class AuthorsView(generic.ListView):
    model = models.Autor
    template_name = "author/authors.html"


class DeleteAuthorsView(generic.DeleteView):
    model = models.Autor
    template_name = "author/delete_author.html"
    success_url = '/success'


class AddAuthorsView(generic.CreateView):
    model = models.Autor
    fields = [
        'autor_name', 'autor_description'
    ]
    template_name = "author/add_author.html"
    success_url = '/success'


class UpdateAuthorsView(generic.UpdateView):
    model = models.Autor
    fields = [
        'autor_name', 'autor_description'
    ]
    template_name = "author/update_author.html"
    success_url = '/success'


# Genre
class GenreListView(generic.ListView):
    model = models.Genre
    template_name = 'genre/genres.html'


class GenreCreateView(generic.CreateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = 'genre/create_genre.html'
    success_url = '/success'


class GenreUpdateView(generic.UpdateView):
    model = models.Genre
    fields = [
        'genre_name', 'genre_description'
    ]
    template_name = 'genre/update_genre.html'
    success_url = '/success'


class GenreDeleteView(generic.DeleteView):
    model = models.Genre
    template_name = 'genre/delete_genre.html'
    success_url = '/success'


# Publishing House
class PublishingHouseView(generic.ListView):
    model = models.PublishingHouse
    template_name = 'house-publishing/houses_publishing.html'


class PublishingHouseCreateView(generic.CreateView):
    model = models.PublishingHouse
    fields = [
        'publishing_house_name', 'publishing_house_description'
    ]
    template_name = 'house-publishing/create_house_publishing.html'
    success_url = '/success'


class PublishingHouseUpdateView(generic.UpdateView):
    model = models.PublishingHouse
    fields = [
        'publishing_house_name', 'publishing_house_description'
    ]
    template_name = 'house-publishing/update_house_publishing.html'
    success_url = '/success'


class PublishingHouseDeleteView(generic.DeleteView):
    model = models.PublishingHouse
    template_name = 'house-publishing/delete_house_publishing.html'
    success_url = '/success'


# Series
class SeriesView(generic.ListView):
    model = models.Series
    template_name = 'series/series.html'


class SeriesCreateView(generic.CreateView):
    model = models.Series
    fields = [
        'series_name', 'series_description'
    ]
    template_name = 'series/create_series.html'
    success_url = '/success'


class SeriesUpdateView(generic.UpdateView):
    model = models.Series
    fields = [
        'series_name', 'series_description'
    ]
    template_name = 'series/update_series.html'
    success_url = '/success'


class SeriesDeleteView(generic.DeleteView):
    model = models.Series
    template_name = 'series/delete_series.html'
    success_url = '/success'


# Books
class BookCreateView(generic.CreateView):
    model = models.Book
    fields = [
        'book_name', 'book_price', 'autor', 'series',
        'genre', 'year_publishing', 'page', 'binding', 'format_book',
        'ISBN', 'weight', 'age_restrictions', 'publishing_house',
        'counter_book', 'active'
    ]
    template_name = 'book/create_book.html'
    success_url = '/success'


class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = [
        'book_name', 'book_price', 'autor', 'series',
        'genre', 'year_publishing', 'page', 'binding', 'format_book',
        'ISBN', 'weight', 'age_restrictions', 'publishing_house',
        'counter_book', 'active'
    ]
    template_name = 'book/update_book.html'
    success_url = '/success'


class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'book/delete_book.html'
    success_url = '/success'


def success_page(request):
    return render(
        request,
        template_name='./success.html'
    )
