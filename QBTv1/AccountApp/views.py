from django.shortcuts import render

def TopPageView(request):
    return render(request, 'TopPage.html')

# Create your views here.
