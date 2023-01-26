from django.contrib import messages
from django.views.generic.edit import FormView
from formapp.forms import QBTForm
from django.shortcuts import render
from django.views.generic import View
from .models import QBTModel
from django.shortcuts import redirect

class TestView(FormView):
    template_name = 'App_Folder_HTML/formpage.html'
    form_class = QBTForm
    success_url = '/QBTsys/Home'  # リダイレクト先URL

    def form_valid(self, form):
        form.save(self.request.user.username)  # 保存処理など
        messages.add_message(self.request, messages.SUCCESS, '登録しました！')  # メッセージ出力
        return super().form_valid(form)


def SetQRparam(request):

    if request.user.is_authenticated:
        if (int(request.GET.get("tempA")) < 43) & (int(request.GET.get("tempA")) > 31) & (int(request.GET.get("tempB")) <= 9) & (int(request.GET.get("tempB")) >= 0):
            post = QBTModel(StudentID=request.user.username, TemperatureA=request.GET.get("tempA"), TemperatureB=request.GET.get("tempB"), Q1=request.GET.get("Q1"), Q2=request.GET.get("Q2"), FreeText='体温計からの記録')
            messages.add_message(request, messages.SUCCESS, '登録しました！')
            post.save()
        else:
            messages.add_message(request, messages.SUCCESS, '不正な値です')

    response = redirect('/QBTsys/Home')
    return response