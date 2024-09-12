from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 

def members(request):
  template = loader.get_template('404.html')
  return HttpResponse(template.render())

def members1(request):
  template = loader.get_template('home-v2.html')
  return HttpResponse(template.render())



