from django.urls import path
from .views import home,gallery,contact
urlpatterns = [
	path('contact/',contact,name='contact_url'),
	path('gallery/',gallery,name='gallery_url'),
    path('',home,name='homePage')
]
