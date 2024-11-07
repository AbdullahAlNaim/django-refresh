from django.shortcuts import render
from django.db import models
from .models import Game
from .forms import AddGame


# Create your views here.
def index(request):


    return render(request, 'landing/index.html')

def info(request):
    model_info = Game.objects.all()

    if request.method == "POST":
        form = AddGame(request.POST)

        if form.is_valid():
            return render(request, 'landing/info.html')

    return render(request, 'landing/info.html', {
        'all_data': model_info
    })

