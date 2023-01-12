from django.urls import path
from . import views
from .views import SetQRparam

urlpatterns = [
    path('QBTForm', views.TestView.as_view(),name="formpage"),
    path('QRcode', SetQRparam ,name="qrcode"),
]
