from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .forms import SignUpForm
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('boards:home')
    else:
        form = SignUpForm()


    return render(request,'signup.html',{'form':form})

# class Redirected_view(TemplateView):
#     template_name = 'logout.html' 


def logout_user(request):
    logout(request)
    return redirect('boards:home')

class UserUpdateView(UpdateView):
    model = User
    fields = ('username','first_name', 'last_name', 'email' )
    template_name = 'myaccount.html'
    success_url = reverse_lazy('accounts:my_account')


    def get_object(self):
        return self.request.user

