from django.urls import path
from portfolio_app.views import *


urlpatterns = [
    path('',index, name='home'),
    path('about/',about,name='about'),
    path('contact/', contact, name='contact'),
    path('hero/', hero, name='hero'),
    path('portfolio/', portfolio, name='portfolio'),
    path('portfolio-details/<int:pk>/', portfolio_details, name='portfolio-details'),
    path('resume/', resume, name='resume'),
    path('skills/', skills, name='skills'),
]