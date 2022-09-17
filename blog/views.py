from django.shortcuts import render, redirect
from django.views.generic import View
from blog.forms import Photoform
from authentification.forms import PhotoprofileUser
from django.contrib.auth.decorators import login_required

from blog.models import Photo


@login_required
def Telechargerphoto(request):
    form = Photoform
    if request.method == "POST":
        form = Photoform(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            return redirect("home")
    return render(request, "blog/add-photo.html", context={
        'form': form
    })


@login_required
def home(request):
    photos = Photo.objects.filter(uploader=request.user)
    return render(request, 'blog/home.html', context={
        "photos": photos
    })

@login_required
def change_profile(request):
    form = PhotoprofileUser(instance=request.user)
    if request.method == "POST":
        form = PhotoprofileUser(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'blog/change-profile.html', context={
        "form": form
    })
