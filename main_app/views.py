import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Gundam, Weapon, Photo
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
  fields = ['name', 'skill', 'description', 'year']
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

def assoc_weapon(request, gundam_id, weapon_id):
  gundam = Gundam.objects.get(id=gundam_id)
  Gundam.weapons.add(weapon_id)
  return redirect('detail', gundam_id=gundam_id)

def unassoc_weapon(request, gundam_id, weapon_id):
  Gundam.objects.get(id=gundam_id).weapons.remove(weapon_id)
  return redirect('detail', gundam_id=gundam_id)


def add_photo(request, gundam_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 instead of using
    # the file name that was sent by the user
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, gundam_id=gundam_id)
    except Exception as e:
      print('An error occured uploading file to S3')
      print(e)
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