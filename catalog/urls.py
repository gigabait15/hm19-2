from django.urls import path
from catalog import views
from catalog.views import home, contact


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]