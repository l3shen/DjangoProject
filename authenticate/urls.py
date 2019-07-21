from django.urls import path
from . import views

urlpatterns = [
	# The app will contain its own URLs!
	path('', views.home, name='home'),
]
