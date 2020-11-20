from django.urls import path
from .views import HomeView, WorldCovid19View, CountryCovid19

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('world-covid19/', WorldCovid19View.as_view(), name = "world-covid19"),
    path('country-covid19/', CountryCovid19.as_view(), name = "country-covid19")
]