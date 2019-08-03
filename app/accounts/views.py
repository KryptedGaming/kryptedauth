# DJANGO IMPORTS
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.apps import apps
from django.contrib.auth.decorators import permission_required, login_required
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.views import PasswordResetConfirmView
from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.models import UserInfo


class UserRegister(FormView):
    template_name = 'accounts/user_register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('accounts-login')

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            is_active=False
        )
        user.save()

        user_info = UserInfo(
            user=user,
            age=form.cleaned_data['age'],
            country=form.cleaned_data['country']
        )
        user_profile.save()
        return super().form_valid(form)


class UserLogin(FormView):
    template_name = 'accounts/user_login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('accounts-login')

    def form_valid(self, form):
        # resolve username from email if needed

        # resolve next url if redirect
        return super().form_valid(form)
