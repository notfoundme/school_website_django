from django.shortcuts import render, redirect
from core.models import *
from core.forms import *


def index(req):
   t= Testimonial.objects.all()
   c = Course.objects.all()
   data = {
      "courseList": c,
      "testimonialList": t
   }
   return render(req,'website/home.html',data)

def aboutUs(req):
   return render(req,'website/about_us.html',{})

def admission(req):
   return render(req,'website/admission.html',{})

def contactUs(req):
   form = ContactForm()
   if req.method == "POST":
      form = ContactForm(req.POST)
      if form.is_valid():
         form.save()
         return redirect("/contact-us")
   data = {
      "form": form
   }
   return render(req,'website/contact_us.html',data)

def downloads(req):
   d = Downloads.objects.all()
   data = {
   "downloads": d
   }
   return render(req,'website/downloads.html',data)

def gallery(req):
   data = Gallery.objects.all()
   return render(req,'website/gallery.html',{
      "gallery": data
   })
   
def news(req):
   data = News.objects.all()
   return render(req,'website/news.html',{
      "newsList": data

   })



