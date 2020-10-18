from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic import View
from django.http import HttpResponseRedirect

from .forms import SignUpForm

# Create your views here.
class SignUpView(View):
    form_class = SignUpForm
    initial = {'key': 'value'}
    template_name = 'accounts/signup.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, self.template_name, {'form':form})