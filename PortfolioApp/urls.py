from django.urls import path

from . import views

# namespace
app_name = 'PortfolioApp'

urlpatterns = [
    path('', views.HelloWorld, name="HelloWorld"),
    path('login/', views.LoginView.as_view(), name='login')
]
