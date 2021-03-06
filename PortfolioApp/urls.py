from django.urls import path

from . import views

# namespace
app_name = 'PortfolioApp'

urlpatterns = [
    path('', views.HelloWorld, name="home"),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('test/',views.test_view),
    path('test1/',views.test_view1),
]
