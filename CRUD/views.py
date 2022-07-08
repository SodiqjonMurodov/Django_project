from django.shortcuts import render
from CRUD.models import Main
import random


def myfunc(request):
    name = ['Sodiq', 'Mirjon', 'Asad', 'Alijon', 'Azizbek', 'Amirbek', 'Ravshan']
    surname = ['Murodov', 'Xakimov', 'Yusupov', 'Shoyev', 'Hikmatov', 'Aliyev']
    desc = ['asdfsdfsdf', 'asdfsff', 'fghththfgh', 'trg65hrther', 'grg56yjghnghfng', 'ert54gryfbsf']
    for x in range(100):
        base = Main.objects.create(
            first_name=random.choice(name),
            last_name=random.choice(surname),
            age=random.randint(1, 100),
            desc=random.choice(desc)
        )
    return render(request, 'index.html', {'base': base})


def rm(request):
    dl = Main.objects.all().delete()
    return render(request, 'index.html', {'del': dl})

def data(request):
    data = Main.objects.all()
    return render(request, 'index.html', {'data': data})
