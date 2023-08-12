from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('rand.gen', views.rand_gen),
    path('timer', views.timer)
]