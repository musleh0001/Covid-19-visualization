from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomeView(TemplateView):
    template_name = 'dashboard/home.html'

@method_decorator(login_required, name='dispatch')
class WorldCovid19View(TemplateView):
    template_name = 'dashboard/world-covid19.html'

@method_decorator(login_required, name='dispatch')
class CountryCovid19(TemplateView):
    template_name = 'dashboard/country-covid19.html'