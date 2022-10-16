from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.entr, name="page"),
    path("create", views.create, name="create"),
    path("rand", views.rand, name="rand"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("search/<str:name>", views.search, name="search"),
]
