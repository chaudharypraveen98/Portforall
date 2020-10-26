from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import FormView

from PortfolioApp.forms import LoginForm, SignUpForm


def HelloWorld(request):
    return render(request, "PortfolioApp/index.html")


def logout_view(request):
    logout(request)
    return redirect('PortfolioApp:home')


class LoginView(FormView):
    form_class1 = LoginForm
    form_class2 = SignUpForm

    template_name = "PortfolioApp/login.html"
    form1 = form_class1(None)
    form2 = SignUpForm(None)

    def get(self, request, **kwargs):
        return render(request, self.template_name, {"login_form": self.form1, "signup_form": self.form2})

    def post(self, request, **kwargs):
        if 'login' in request.POST:
            form = self.form_class1(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('PortfolioApp:home')
            print(form.errors)
        elif 'signup' in request.POST:
            form = self.form_class2(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                print("user created successfully")
                user.save()
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('PortfolioApp:home')
            print(form.errors)
        return render(request, self.template_name, {"login_form": self.form1, "signup_form": self.form2})


def test_view(request):
    return render(request,'PortfolioApp/template1.html')