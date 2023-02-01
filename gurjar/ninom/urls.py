from django.contrib import admin
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="Home page"),
    path('about',views.about,name="About page"),
    path('fruit',views.fruit,name="Fruit page"),
    path('contact',views.contact,name="Contact page"),
    path('testimonial',views.testimonial,name="Testimonial page"),
   
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)