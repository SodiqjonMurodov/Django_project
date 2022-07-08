from django.shortcuts import render
from .models import Fruits


def myfunc(request):
    value = Fruits.objects.all()
    return render(request, 'base.html', {'key': value})


def main(request, raqam):
    print(raqam)
    base = Fruits.objects.get(id=raqam)
    return render(request, 'main.html', {'base': base})
