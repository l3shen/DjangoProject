from django.shortcuts import render

def home(request):
	# Requesting a web page, must pass in to the function.
	return render(request, 'authenticate/home.html', {}) # Pass in location.

	
