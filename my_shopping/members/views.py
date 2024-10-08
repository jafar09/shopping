from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render 
from store.models import Product
def main(request):
  return render(request, "main.html")

def members(request):
  return render(request,"404.html")

def about(request):
  return render(request,"about.html")

def contactv1(request):
  return render(request,"contact-v1.html")

def contactv2(request):
  return render(request,"contact-v2.html")

def faq(request):
  return render(request,"faq.html")

def homev2(request):
  products = Product.objects.filter(is_available=True)
  context = {
    'products': products
  }
  return render(request,"home-v2.html" , context)


def homev3fullcolorbg(request):
  return render(request,"home-v3-full-color-bg.html")

def homev3(request):
  return render(request,"home-v3.html")

def homev4(request):
  return render(request,"home-v4.html")

def homev5(request):
  return render(request,"home-v5.html")

def homev6(request):
  return render(request,"home-v6.html")

def homev7(request):
  return render(request,"home-v7.html")

def storedirectory(request):
  return render(request,"store-directory.html")

def termsandconditions(request):
  return render(request,"terms-and-conditions.html")


def yangilik(request, id):
  if id > 0 and id < 4:
    yangiliklar = [
      "yangilik 1",
      "yangilik 2",
      "yangilik 3",
    ]
    return HttpResponse( yangiliklar [id-1])
  else:
      return HttpResponse("Bunday yangilik yuq")

