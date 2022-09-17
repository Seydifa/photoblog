from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import Photoform, Blogform, DeleteBlogform
from authentification.forms import PhotoprofileUser
from django.contrib.auth.decorators import login_required
from blog.models import Photo, Blog


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
    blogs = Blog.objects.filter(autheur=request.user)
    return render(request, 'blog/home.html', context={
        "photos": photos,
        "blogs": blogs
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


@login_required
def blog_photo_upload(request):
    blogform = Blogform()
    photoform = Photoform()
    if request.method == "POST":
        photoform = Photoform(request.POST, request.FILES)
        blogform = Blogform(request.POST)
        if all([photoform.is_valid(), blogform.is_valid()]):
            photo = photoform.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blogform.save(commit=False)
            blog.autheur = request.user
            blog.photo = photo
            blog.save()
            redirect('home')
    return render(request, "blog/blog-photo.html", context={
        "blogform": blogform,
        "photoform": photoform
    })

@login_required
def get_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog/blog-details.html', context={
        "blog": blog
    })


@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    edit_form = Blogform(instance=blog)
    delete_blog_form = DeleteBlogform()
    if request.method == 'POST':
        pass
    return render(request, 'blog/edit-blog.html', context={
        "edit_form": edit_form,
        "delete_blog_form": delete_blog_form
    })