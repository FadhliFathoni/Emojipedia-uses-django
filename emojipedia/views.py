from django.shortcuts import render, redirect
from .models import EmojiModels
from .forms import EmojiForm

def list(request):
    form = EmojiModels.objects.all()
    context = {
        "heading":"Emojipedia",
        "form":form
    }
    return render(request,'list.html',context)

def create(request):
    form = EmojiForm(request.POST or None)
    context = {
        "heading":"Create",
        "form":form
    }
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("list")
    return render(request,'create.html',context)

def delete(request, delete_id):
    EmojiModels.objects.filter(id=delete_id).delete()
    return redirect('list')

def update(request, update_id):
    akun = EmojiModels.objects.get(id=update_id)
    data = {
        "emoji":akun.emoji,
        "nama":akun.nama,
        "keterangan":akun.keterangan,
    }
    form = EmojiForm(request.POST or None, initial=data, instance=akun)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "heading":"Update",
        "form":form,
    }
    return render(request,"create.html",context)
