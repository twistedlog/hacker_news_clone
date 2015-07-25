from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import UserCreateForm
# Create your views here.


class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    success_url = '/posts/'
    form_class = UserCreateForm