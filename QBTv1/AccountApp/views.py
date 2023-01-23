from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from formapp.models import QBTModel

def TopPageView(request):
    return render(request, 'TopPage.html')

#ホーム
class HomeView(TemplateView):
    template_name = 'TopPage.html'

#登録
class UserCreateView(CreateView):
    template_name = 'user_create.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('AccountApp:home')

#ログアウト
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'TopPage.html'

#登録状況
def QBTdetailView(request):
    ctx = {}
    SID = request.user.username
    q = QBTModel.objects.filter(StudentID=SID).order_by('created_at').reverse()
    user_dict = {'QBTdet': q}
    return render(request, 'QBTdetail.html', context=user_dict)