from django.urls import path
from . import views

urlpatterns = [
    path('',views.HelloWorld,name="HelloWorld")
]
