"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    # Autor
    path('authors/', views.AuthorsView.as_view(), name="authors"),
    path('add_author/', views.AddAuthorsView.as_view(), name="add-author"),
    path('delete_author/<int:pk>/', views.DeleteAuthorsView.as_view(), name="delete-author"),
    path('update_author/<int:pk>/', views.UpdateAuthorsView.as_view(), name="update-author"),
    # Genre
    path('genres/', views.GenreListView.as_view(), name="genres"),
    path('create_genre/', views.GenreCreateView.as_view(), name="create-genre"),
    path('delete_genre/<int:pk>/', views.GenreDeleteView.as_view(), name="delete-genre"),
    path('update_genre/<int:pk>/', views.GenreUpdateView.as_view(), name="update-genre"),
    # Publishing house
    path('publishing_houses/', views.PublishingHouseView.as_view(), name="houses-publishing"),
    path('create_publishing_house/', views.PublishingHouseCreateView.as_view(), name="create-publishing-house"),
    path('delete_publishing_house/<int:pk>/', views.PublishingHouseDeleteView.as_view(),
         name="delete-publishing-house"),
    path('update_publishing_house/<int:pk>/', views.PublishingHouseUpdateView.as_view(),
         name="update-publishing-house"),
    # Series
    path('series/', views.SeriesView.as_view(), name="series"),
    path('create_series/', views.SeriesCreateView.as_view(), name="create-series"),
    path('delete_series/<int:pk>/', views.SeriesDeleteView.as_view(), name="delete-series"),
    path('update_series/<int:pk>/', views.SeriesUpdateView.as_view(), name="update-series"),
    # Books
    path('create_book/', views.BookCreateView.as_view(), name="create-book"),
    path('view_book/<int:pk>', views.ViewBook.as_view(), name="view-book"),
    path('delete_book/<int:pk>/', views.BookDeleteView.as_view(), name="delete-book"),
    path('update_book/<int:pk>/', views.BookUpdateView.as_view(), name="update-book"),

    path('success', views.success_page)
]
