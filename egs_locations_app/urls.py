from django.urls import path
from . import views


urlpatterns = [
    path('', views.PlayfieldView.as_view(), name='playfields'),
]