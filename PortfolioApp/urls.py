from django.urls import path

from . import views

# namespace
app_name = 'PortfolioApp'

urlpatterns = [
    path('home', views.HelloWorld, name="home"),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('signup/', views.signup, name='signup'),

]
