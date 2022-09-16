from django.shortcuts import render
from django.views.generic import View
from blog.forms import Photomodel


class Techargerphoto(View):
    template_name = "blog/add-photo.html"
    form_classe = Photomodel

    def get(self, request):
        pass

    def post(self, request):
        pass