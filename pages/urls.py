# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, hannahPageView, results, homePost

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('hannah/', hannahPageView, name='hannah'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
