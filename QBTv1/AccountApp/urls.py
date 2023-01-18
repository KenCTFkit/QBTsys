from django.urls import path

from . import views
from django.urls import include
app_name = 'AccountApp'

urlpatterns = [
    path('forms/', include('formapp.urls'), name="forms"),
    path('Home', views.TopPageView ,name="home"),
    path('user_create', views.UserCreateView.as_view(), name="user_create"),
    path('login', include('LoginApp.urls'), name="login"),
    path('logout', views.LogoutView.as_view(), name="logout"),
]