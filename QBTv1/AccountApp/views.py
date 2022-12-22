from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

def TopPageView(request):
    return render(request, 'TopPage.html')

#アカウント作成

#トップページを表示する処理
class HomeView(TemplateView):
    template_name = 'TopPage.html'

#会員登録ページに関する処理
class UserCreateView(CreateView):
    template_name = 'user_create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')