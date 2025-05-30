from django.urls import path
from . import views

app_name = "appsenac"

urlpatterns = [
    path("", views.home, name="home"),
    path("contatos/", views.contatos, name="contatos"),
    path("sobre_senac/", views.sobre_senac, name="sobre_senac"),
]
