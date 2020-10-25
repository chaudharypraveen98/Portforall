from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView
from PortfolioApp.forms import LoginForm, SignUpForm


def HelloWorld(request):
    return render(request, "index.html")


class LoginView(FormView):
    form_class1 = LoginForm
    form_class2 = SignUpForm

    template_name = "PortfolioApp/login.html"
    form1 = form_class1(None)
    form2 = SignUpForm(None)

    def get(self, request, **kwargs):
        return render(request, self.template_name, {"form": self.form1, "signupform":self.form2})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('PortfolioApp:HelloWorld')
        return render(request, self.template_name, {"form": form,"signupform":form2})


def signup(request):
    if request.method == 'post':
        email = request.POST["email"]
        username = request.POST["username"]
        password = request.POST["password"]
