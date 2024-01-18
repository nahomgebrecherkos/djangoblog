from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpFrom, UserUpdateFrom, ProfileUpdateForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = SignUpFrom()
    context = {
        'form': form
    }
    return render(request, 'users/sign_up.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateFrom(request.POST or None, instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            return redirect('users-profile')
    else:
        u_form = UserUpdateFrom(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)