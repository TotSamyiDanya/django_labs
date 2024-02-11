import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForm
from .models import Book


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def game(request):
    return render(request, "game.html")


def form(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_data = user_form.cleaned_data
            with open('myapp/static/users.txt', 'a', encoding='utf-8') as file:
                file.write(f'Name: {user_data['name']}; Surname: {user_data['surname']}; '
                           f'Patronymic: {user_data['patronymic']}; Faculty: {user_data['faculty']}; '
                           f'Age: {user_data['age']}; Agreement: {user_data['agreement']}\n')
            return render(request, 'thanks.html', {'data': user_data})
    else:
        user_form = UserForm()
    return render(request, "form.html", {"form": user_form})


def thanks(request):
    return render(request, "thanks.html")


def map(request):
    return render(request, "map.html")


def video(request):
    return render(request, "video.html")


def text(request):
    return render(request, "text.html")


def books(request):
    books_collection = Book.objects.all()
    return render(request, "books.html", {'data': books_collection})


def image(request):
    return render(request, "image.html")
