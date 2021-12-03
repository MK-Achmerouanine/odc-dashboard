from django.urls import path
from .views import index, index_two
urlpatterns = [
    path('', index),
    path('two/', index_two),
]
