from django.shortcuts import render
from django.http import HttpResponse

class Gundam:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, skill, description, year):
    self.name = name
    self.skill = skill
    self.description = description
    self.year = year

gundams = [
  Gundam('Deathsythe Hell', 'Stealth', 'Variant of the grim reaper', 195),
  Gundam('Heavyarms', 'Firepower', 'Suited for long range tactics', 195),
  Gundam('Sandrock', 'Desert Specialist', 'Designed as commander due to strengths in advanced communications/ analysis systems', 195)
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gundams_index(request):
    return render(request, 'gundams/index.html', {
        'gundams': gundams
    }) 