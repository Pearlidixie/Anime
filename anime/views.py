from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Mage, Shinobi, User
from .forms import PostMage, UserReg


# Create your views here.

def index(request):
    mages = Mage.objects.order_by('mage_name')
    shinobis = Shinobi.objects.order_by('shinobi_name')
    return render(request, 'anime/index.html', {'mages': mages, 'shinobis': shinobis})

def mage_detail(request, pk):
    mage = get_object_or_404(Mage, pk=pk)
    return render(request, 'anime/mage_detail.html', {'mage': mage})

def add_new(request):
    if request.method == "POST":
        form = PostMage(request.POST)
        if form.is_valid():
           mage = form.save()
           mage.save()
           return redirect('mage_detail', pk=mage.pk)
    else:
        form = PostMage()
    return render(request, 'anime/mage_edit.html', {'form': form})

def add_user(request):
    if request.method == "POST":
        form = UserReg(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('index')
    else:
        form = UserReg()
    return render(request, 'anime/user_add.html', {'form': form})


def myMages(request):
     mage_list = Mage.objects.all()
     output = ','.join([m.mage_name for m in mage_list])
     return HttpResponse(output)
