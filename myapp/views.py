from django.shortcuts import render


# Create your views here.

def myFunc(request):
    return render(request, 'base.html')
