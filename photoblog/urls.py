from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from authentification.views import SignUp
from blog.views import Telechargerphoto, home, change_profile, blog_photo_upload, get_blog
from photoblog import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", LoginView.as_view(
        template_name='authentification/login.html',
        redirect_authenticated_user=True,
        next_page='home'
    ), name='se-connecter'),
    path("logout", LogoutView.as_view(
        next_page="se-connecter"
    ), name='se-deconnecter'),
    path("home", home, name='home'),
    path("change-password", PasswordChangeView.as_view(
        template_name="authentification/changeMotdepasse.html",
        success_url="change-password-done"
    ), name='changepassord'),
    path('change-password-done', PasswordChangeDoneView.as_view(
        template_name="authentification/password-change-done.html"
    ), name='change-password-done'),
    path('signUp', SignUp.as_view(),
         name='signup'),
    path('photo/uploader', Telechargerphoto,
         name="photo-uploader"),
    path("change-profile", change_profile, name="change-profile"),
    path("blog/post/upload", blog_photo_upload, name='blog-photo-upload'),
    path("blog/<int:blog_id>", get_blog, name="blog-detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
