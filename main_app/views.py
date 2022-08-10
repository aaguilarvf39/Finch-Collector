from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gundam
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
   repair_form = RepairsForm()
   return render(request, 'gundams/detail.html', {
     'gundam': gundam, 'repair_form': repair_form 
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
