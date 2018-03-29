from django.contrib.auth import get_user_model, logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, View

from .forms import RegisterForm
# Create your views here.
User = get_user_model()

class UserRegisterView(CreateView):
	form_class = RegisterForm
	template_name = 'profiles/register.html'
	success_url = '/login'

	def dispatch(self, *args, **kwargs):
		if self.request.user.is_authenticated:
			self.request.user.is_active = True
			return redirect('/logout')
		return super(UserRegisterView, self).dispatch(*args, **kwargs)

def logout_view(request):
    logout(request)
    return redirect('/login')

def login_view(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		print(username)
		print(password)
		user = authenticate(username=username, password=password)

		if user:
			login(request, user)
			return HttpResponseRedirect('/teams/')
		else:
			print("not user")
			return render(request, 'profiles/login.html')
	return render(request, 'profiles/login.html')