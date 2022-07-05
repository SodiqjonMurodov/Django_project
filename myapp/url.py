from django.urls import path
from .views import myFunc

urlpatterns = [
    path('', myFunc),

]