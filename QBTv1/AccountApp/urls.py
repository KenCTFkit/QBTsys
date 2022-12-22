from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('Forms/', include('formapp.urls')),
    path('Home', views.TopPageView ,name="home"),
    path('user_create', views.UserCreateView.as_view(), name="user_create"),#会員登録ページへのパス
]
