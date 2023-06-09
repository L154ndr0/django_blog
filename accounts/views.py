from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.

class SingUpView(CreateView):
    form_class = UserCreationForm
    template_name ='registration/signup.html'
    success_url = reverse_lazy('login')
