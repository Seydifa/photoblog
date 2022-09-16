from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentification.forms import Loginform, Signupform
from django.contrib.auth.decorators import login_required
from django.views.generic import View


class LoginPage(View):
    formulaire_classe = Loginform
    template_classe = 'authentification/login.html'

    def get(self, request):
        formulaire = self.formulaire_classe()
        message = ""
        return render(request, self.template_classe, context={
            "formulaire": formulaire,
            "message": message
        })

    def post(self, request):
        formulaire = self.formulaire_classe(request.POST)
        message = ""
        if formulaire.is_valid():
            user = authenticate(**formulaire.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = f"Nom d'utilisateur ou mot de passe invalide !"

        return render(request, self.template_classe, context={
            "formulaire": formulaire,
            "message": message
        })


def logout_user(request):
    logout(request)
    return redirect('se-connecter')

@login_required
def home(request):
    return render(request, 'home.html')


class SignUp(View):
    form_class = Signupform
    template_name = 'authentification/signup.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={
            'form':form
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

        return render(request, self.template_name, context={
            'form':form
        })