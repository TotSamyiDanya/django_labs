from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, template_name="index.html")


def about(request):
    return render(request, template_name="about.html")


def game(request):
    return render(request, template_name="game.html")