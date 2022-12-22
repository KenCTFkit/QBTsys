from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import ContactForm

def index_template(request):
    form = ContactForm()
    return render(request, 'index.html', {
        'form': form,
    })
