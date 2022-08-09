from django.shortcuts import render
from .models import Gundam

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
   return render(request, 'gundams/detail.html', { 'gundam': gundam })
