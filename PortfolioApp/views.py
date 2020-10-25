from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView

from PortfolioApp.forms import LoginForm, RegisterForm


def HelloWorld(request):
    return render(request, "index.html")


class LoginView(FormView):
    form_class = LoginForm
    template_name = "PortfolioApp/login.html"

    def get(self, request, **kwargs):
        form = self.form_class(None)
        return render(request, self.template_name, {"form": form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('PortfolioApp:HelloWorld')
        return render(request, self.template_name, {"form": form})


def signup(request):
    if request.method == 'post':
        username = request.POST["username"]
        password = request.POST["username"]
        email = request.POST["email"]
