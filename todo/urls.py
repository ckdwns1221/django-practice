from django.urls import path
from .views import todos, index

urlpatterns = [
    path('', todos),
    path('index/', index)
]