from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'core/home.html'

def home(request):
    return render(request, 'core/home.html')
