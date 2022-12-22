from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('Forms/', include('formapp.urls')),
    path('Home', views.TopPageView ,name="TopPage"),
]
