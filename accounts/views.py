from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ProfileForm, MyPasswordChangeForm



def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:profile')
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


def profile(request):

    return render(request, 'accounts/profile.html')

# @login_required
# def edit_profile(request):
#     return render(request, 'accounts/edit_profile.html')


def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            messages.error(request,('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form})



def change_password(request):
    form = MyPasswordChangeForm(request.user)
    if request.method == 'POST':
        form = MyPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been updated!')
            return HttpResponseRedirect(reverse('accounts:profile'))
    return render(request, 'accounts/change_password.html', {'form': form})
