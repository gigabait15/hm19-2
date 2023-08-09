from django.urls import path
from catalog.views import *


urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
]