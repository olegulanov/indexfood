from django.shortcuts import redirect, render
from .models import Task, FIO, Tovar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, get_user_model
from .utils import * 
from .forms import *


# Create your views here.
def mainpage(request):
    tasks = Task.objects.all()
    all_data = Tovar.objects.all()
    return render(request, 'main/mainpage.html', {'tasks':tasks, 'data_tovar':all_data,})

def about(request):
    filter = FIO.objects.all()

    return render(request, 'main/about.html', {'filterN':filter}) #,'amount_data':amount_data})

    
# def about(request):
#     all_data = Tovar.objects.all()
#     return render(request, 'main/about.html', {'data_tovar':all_data})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items())+list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('Home')


def logout_user(request):
    logout(request)
    return redirect('login')


