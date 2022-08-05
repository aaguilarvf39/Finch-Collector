from django.shortcuts import render
from django.http import HttpResponse

class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.type = type
    self.description = description
    self.age = age

finches = [
  Finch('Garuda', 'society finch', 'warrior bird', 5),
  Finch('Taka', 'owl finch', 'relentless', 7),
  Finch('Shisui', 'blue finch', 'swift', 3)
]

# Create your views here.
def home(request):
    return HttpResponse('<h1>*Chirp* (*v*) *Chirp*</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    }) 