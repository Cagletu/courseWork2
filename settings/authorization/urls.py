from django.urls import path
from . import views

app_name = 'authorization'

urlpatterns = [

    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),

    path("add_to_cart/<int:pk>/", views.AddToCartView.as_view(), name="add_to_cart"),
]
