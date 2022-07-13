from django.shortcuts import render
from CRUD.models import Main
import random


def myfunc(request):
    name = ['Sodiq', 'Mirjon', 'Asad', 'Alijon', 'Azizbek', 'Amirbek', 'Ravshan']
    surname = ['Murodov', 'Xakimov', 'Yusupov', 'Shoyev', 'Hikmatov', 'Aliyev']
    desc = ['asdfsdfsdf', 'asdfsff', 'fghththfgh', 'trg65hrther', 'grg56yjghnghfng', 'ert54gryfbsf']
    for x in range(100):
        Main.objects.create(
            first_name=random.choice(name),
            last_name=random.choice(surname),
            age=random.randint(1, 100),
            desc=random.choice(desc)
        )
    data = Main.objects.all()
    return render(request, 'index.html', {'data': data})


def rm(request):
    Main.objects.all().delete()
    return render(request, 'index.html')


def second(request):
    number = request.POST.get('int')
    a = Main.objects
    base = a.filter(age__gt=number)
    maks = a.aggregate(base)
    count = base.count()
    return render(request, 'second.html', {'base': base, 'count': count, 'maks': maks})


def third(request):
    return render(request, 'second.html')
