from django.contrib import messages
from django.views.generic.edit import FormView
from formapp.forms import QBTForm
from django.shortcuts import render
from django.views.generic import View
from .models import User

class TestView(FormView):
    template_name = 'App_Folder_HTML/formpage.html'
    form_class = QBTForm
    success_url = '/QBTsys/Home'  # リダイレクト先URL

    def form_valid(self, form):
        form.save()  # 保存処理など
        messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        return super().form_valid(form)


def SetQRparam(request):
    post = User(StudentID='170127', TemperatureA=39, TemperatureB=2, Q1=0, Q2=0, FreeText='FreeText')
    post.save() 
    return render(request, 'TopPage.html')