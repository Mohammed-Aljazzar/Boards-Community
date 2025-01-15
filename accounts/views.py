from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from .forms import SignUpForm
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UserForm, UserProfileForm
# Create your views here.
from .models import UserProfile

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

# def profile_update(request):
#     if request.method =='POST':
#         user_form = UserForm(request.POST,instance=request.user)
#         profile_form = UserProfileForm(request, request.FILES , instance=request.user.profile)
#         if user_form.is_valid and profile_form.is_valid :
#             user_form.save()
#             profile_form.save()
#             return redirect('accounts:my_account')
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = UserProfileForm(instance=request.user.profile)
#         return render(request,'myaccount.html',{'user_form':user_form, 'profile_form':profile_form})

def profile_update(request):
    # Get or create the UserProfile
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:my_account')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'myaccount.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })