from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import UserRegistrationForm

class HomeView(TemplateView):
    template_name = 'core/home.html'

@login_required
def home(request):
    return render(request, 'core/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'redirect_url': '/'})
            messages.success(request, 'Kayıt başarılı!')
            return redirect('home')
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        messages.error(request, 'Kayıt başarısız. Lütfen hataları düzeltin.')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})