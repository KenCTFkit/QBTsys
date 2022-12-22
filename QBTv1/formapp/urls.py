from django.urls import path
from . import views

urlpatterns = [
    path('QBTForm', views.TestView.as_view(),name="formpage"),
]
