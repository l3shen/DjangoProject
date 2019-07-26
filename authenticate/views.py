from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import signup_form


def home(request):
	# Requesting a web page, must pass in to the function.
	return render(request, 'authenticate/home.html', {}) # Pass in location.

def login_user(request):
	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
    	
		if user is not None:
			login(request, user)
			messages.success(request, ('You have successfully logged in.'))
			# Redirect to the home page for now.
			return redirect('home')
		else:
			messages.success(request, ('Error. Please try again.'))
			return redirect('login')

	else:
		return render(request, 'authenticate/login.html', {}) # Pass in location.

def logout_user(request):
	logout(request)
	messages.success(request, ('Successfully logged out.'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = signup_form(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# Automatically login the user upon registration.
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('You have successfully registered.'))
			return redirect('home')
	else:
		form = signup_form()

	# Creat form from user data via POST.
	context = {'form': form}

	# Pass into the registration page and render.
	return render(request, 'authenticate/register.html', context)