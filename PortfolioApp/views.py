from django.shortcuts import render

def HelloWorld(request):
    return render(request,"index.html")
