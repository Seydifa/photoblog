from django.shortcuts import render, redirect
from django.views.generic import View
from blog.forms import Photoform
from django.contrib.auth.decorators import login_required


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
