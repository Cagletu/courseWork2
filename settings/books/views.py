from pathlib import Path

from PIL import Image
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
        'book_name', 'book_image', 'book_price', 'autor', 'series',
        'genre', 'year_publishing', 'page', 'binding', 'format_book',
        'ISBN', 'weight', 'age_restrictions', 'publishing_house',
        'counter_book', 'active'
    ]
    template_name = 'book/create_book.html'
    success_url = '/success'


class BookUpdateView(generic.UpdateView):
    model = models.Book
    fields = [
        'book_name', 'book_image', 'book_price', 'autor', 'series',
        'genre', 'year_publishing', 'page', 'binding', 'format_book',
        'ISBN', 'weight', 'age_restrictions', 'publishing_house',
        'counter_book', 'active'
    ]
    template_name = 'book/update_book.html'
    success_url = '/success'

    def get_success_url(self) -> str:
        resizer(self.object.book_image)
        return super().get_success_url()


class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = 'book/delete_book.html'
    success_url = '/success'


def resizer(image):
    extention = image.file.name.split('.')[-1]
    BASE_DIR = Path(image.file.name).resolve().parent
    file_name = Path(image.file.name).resolve().name.split('.')
    for m_basewidth in [250, 40]:
        im = Image.open(image.file.name)
        wpercent = (m_basewidth / float(im.size[0]))
        hsize = int(float(im.size[1]) * float(wpercent))
        im.thumbnail((m_basewidth, hsize), Image.Resampling.LANCZOS)
        im.save(str(BASE_DIR / "".join(file_name[:-1])) + f'_{m_basewidth}.' + extention)


def success_page(request):
    return render(
        request,
        template_name='./success.html'
    )
