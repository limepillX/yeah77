import datetime
from django.shortcuts import render, redirect
from .models import *

from mainapp.forms import *


def list_data(request):
    return render(request, 'list.html', {'alldata': Data.objects.all()})


def index(request):
    if request.method == 'POST':
        form = AddDataForm(request.POST)
        if form.is_valid():
            print(form.data['data'])
            Data(name={f'{datetime.datetime.now()}': form.data['data']}).save()
            return redirect('list')
    else:
        form = AddDataForm()
    return render(request, 'index.html', {'form': form})
