from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, views
from .forms import (
    SignUpForm,
    NewUserForm
)
from django.contrib.auth.models import User
from django.views.generic.list import ListView


def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        #password = form.cleaned_data.get('password1')
        #user = authenticate(username=user.username, password=password)
        #login(request, user)
        return redirect('/accounts')
    return render(request, 'CustomUsers/signup.html', {'form': form})

def home_view(request):
    return render(request, 'CustomUsers/home.html')

class login_view(views.LoginView):
    template_name = 'CustomUsers/login.html'

class SUview(ListView):
    template_name = 'CustomUsers/newusers.html'
    queryset = User.objects.all().filter(is_active=False)
    form_class = NewUserForm
    context_object_name = 'users'
    sucess_url = "new_users"

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.username = self.request.user
        return super().form_valid(form)

    
    