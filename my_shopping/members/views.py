from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('exx.html')
  return HttpResponse(template.render())

def members1(request):
  template = loader.get_template('home-v2.html')