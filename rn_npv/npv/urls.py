from django.urls import path

from . import views


app_name = 'rn'

urlpatterns = [
    path('', views.index, name='npv'),
]
