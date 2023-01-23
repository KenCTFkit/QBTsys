from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('', views.Account_login.as_view(), name="login"),#会員登録ページへのパス
    
]
