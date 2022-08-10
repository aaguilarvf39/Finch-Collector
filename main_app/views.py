from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Gundam, Weapon
from .forms import RepairsForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gundams_index(request):
    gundams = Gundam.objects.all()
    return render(request, 'gundams/index.html', {'gundams': gundams })


def gundams_detail(request, gundam_id):
   gundam = Gundam.objects.get(id=gundam_id)
   id_list = gundam.weapons.all().values_list('id')
   weapons_gundam_doesnt_have = Weapon.objects.exclude(id__in=id_list)
   repair_form = RepairsForm()
   return render(request, 'gundams/detail.html', {
     'gundam': gundam, 'repair_form': repair_form, 'weapons': weapons_gundam_doesnt_have
    })

class GundamCreate(CreateView):
  model = Gundam
  fields = '__all__'
  success_url = '/gundams/'

class GundamUpdate(UpdateView):
  model = Gundam
  # Let's disallow the renaming of a gundam by excluding the name field!
  fields = ['skill', 'description', 'year']

class GundamDelete(DeleteView):
  model = Gundam
  success_url = '/gundams/'

def add_repair(request, gundam_id):
  form = RepairsForm(request.POST)
  # validate the form
  if form.is_valid():
    new_repair = form.save(commit=False)
    new_repair.gundam_id = gundam_id
    new_repair.save()
  return redirect('detail', gundam_id=gundam_id)

class WeaponList(ListView):
  model = Weapon

class WeaponDetail(DetailView):
  model = Weapon

class WeaponCreate(CreateView):
  model = Weapon
  fields = '__all__'

class WeaponUpdate(UpdateView):
  model = Weapon
  fields = ['name', 'info']

class WeaponDelete(DeleteView):
  model = Weapon
  success_url = '/weapons/'