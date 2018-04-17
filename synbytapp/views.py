from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
#from .mixins import StaffRequiredMixin
from django.core.exceptions import ImproperlyConfigured
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic 

from .models import (
		SliderImage, 
		Portfolio, 
		Testimonials, 
		Services, 
		VoiceAndCarrier,
		AboutUs, 
		Support, 
		TermsOfUse)

def home(request):
	slider_image = SliderImage.objects.all()
	portfolio_object = Portfolio.objects.all()[0:6]
	service_object = Services.objects.all()[0:6]
	testimonial_object = Testimonials.objects.all()[0:10]
	context = {
		"slider_image": slider_image,
		"portfolio_object": portfolio_object,
		"testimonial_object": testimonial_object,
		"service_object": service_object,
	}
	return render(request, 'index.html', context)
	
def about(request):
	title = AboutUs.objects.all()
	return render(request, 'about.html', {'title': title})	
	
def blog(request):
	return render(request, 'blog.html')	
	
def support(request):
	title = Support.objects.all()
	return render(request, 'support.html', {'title': title})	
	
def terms_of_use(request):
	title = TermsOfUse.objects.all()
	return render(request, 'terms_of_use.html', {'title': title})
	
class SliderImageListView(ListView):
	model = SliderImage
	queryset = SliderImage.objects.all()
	
class PortfolioListView(generic.ListView):
	model = Portfolio
	queryset = Portfolio.objects.all()
	
class TestimonialsListView(ListView):
	model = Testimonials
	queryset = Testimonials.objects.all()
	
class ServicesListView(ListView):
	model = Services
	queryset = Services.objects.all()
	
class VoiceListView(ListView):
	model = VoiceAndCarrier
	queryset = Services.objects.all()

	

	
	