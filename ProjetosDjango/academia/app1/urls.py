from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path("", views.home, name="home"),
    path("produtos/", views.produtos, name="produtos"),
    path("contatos/", views.contatos, name="contatos"),
    path("add-produto/", views.add_produto, name="add_produto"),
    path("upload-profile/", views.upload_profile, name="upload_profile"),
    path('matricula/', views.matricula, name='matricula'),
    path('matricula/sucesso/', views.matricula_sucesso, name='matricula_sucesso'),
]
