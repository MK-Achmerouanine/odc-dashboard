from django.shortcuts import render
from .models import Seance


def index(request):
    seances = Seance.objects.all()
    context = {
        'title': 'Dashboard Homepage',
        'seances': seances
    }
    return render(request, 'index.html', context)

def index_two(request):
    seances = Seance.objects.all()
    context = {
        'title': 'Dashboard page 2',
        'seances': seances
    }
    return render(request, 'dash-2.html', context)
