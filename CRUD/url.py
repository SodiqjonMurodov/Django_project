from django.urls import path

from CRUD import views

urlpatterns = [
    path('', views.myfunc, name='func'),
    path('rm', views.rm, name='dl'),
    path('sec', views.second, name='sec'),
    path('third', views.third, name='third')
]
