from django.shortcuts import render

from .models import MovieModel


def index(request):
    movie_model_list = MovieModel.objects.all()
    context = {'movie_model_list': movie_model_list}
    return render(request, 'movie_app/index.html', context)


def dark(request):
    movie_model_list = MovieModel.objects.all()
    context = {'movie_model_list': movie_model_list}
    return render(request, 'movie_app/newIndex.html', context)