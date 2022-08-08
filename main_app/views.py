from django.shortcuts import render
from django.http import HttpResponse

class Gundam:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

gundams = [
  Gundam('Garuda', 'society mecha', 'warrior bird', 5),
  Gundam('Taka', 'owl mecha', 'relentless', 7),
  Gundam('Shisui', 'blue mecha', 'swift', 3)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Mobile Suit Gundam Wing</h1>')

def about(request):
  return render(request, 'about.html')

def gundams_index(request):
    return render(request, 'gundams/index.html', {
        'gundams': gundams
    }) 