from django.shortcuts import render, get_object_or_404, redirect
from .models import Personel
from .forms import PersonelForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def personel_list(request):
    q = request.GET.get("q", "")
    aktif = request.GET.get("aktif", "")
    personeller = Personel.objects.all()
    if q:
        personeller = personeller.filter(ad__icontains=q) | personeller.filter(pozisyon__icontains=q)
    if aktif in ["0", "1"]:
        personeller = personeller.filter(aktif=bool(int(aktif)))
    form = PersonelForm()
    return render(request, 'personel/list.html', {'personeller': personeller, 'form': form})

@login_required
def personel_detail(request, pk):
    personel = get_object_or_404(Personel, pk=pk)
    return render(request, 'personel/detail.html', {'personel': personel})



@login_required
def personel_create(request):
    form = PersonelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Yeni personel başarıyla eklendi.")
        return redirect('personel_list')
    return render(request, 'personel/form.html', {'form': form, 'baslik': 'Yeni Personel Ekle'})

@login_required
def personel_update(request, pk):
    personel = get_object_or_404(Personel, pk=pk)
    form = PersonelForm(request.POST or None, instance=personel)
    if form.is_valid():
        form.save()
        messages.success(request, "Personel bilgileri güncellendi.")
        return redirect('personel_list')
    return render(request, 'personel/form.html', {'form': form, 'baslik': 'Personeli Düzenle'})

@login_required
def personel_delete(request, pk):
    personel = get_object_or_404(Personel, pk=pk)
    if request.method == 'POST':
        personel.delete()
        messages.success(request, "Personel silindi.")
        return redirect('personel_list')
    return render(request, 'personel/confirm_delete.html', {'personel': personel})
