from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("game", views.game, name="game"),
    path("form", views.form, name="form"),
    path("thanks", views.thanks, name="thanks"),
    path("map", views.map, name="map"),
    path("video", views.video, name="video"),
    path("text", views.text, name="text"),
    path("books", views.books, name="books"),
    path("image", views.image, name="image")

]
