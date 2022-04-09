from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .forms import SignUpForm, SignInForm


def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, 'Account created successfully!')

            # form.save()
            return redirect('sign_in')

        # username = request.POST.get('username')
        # first_name = request.POST.get('first_name')
        # last_name = request.POST.get('last_name')
        # email = request.POST.get('email')
        # password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password')

        # if password == confirm_password:
        #     new_user = User.objects.create_user(
        #         username=username,
        #         first_name=first_name,
        #         last_name=last_name,
        #         email=email,
        #     )
        #     # set_password IS USE FOR HASING PASSWORD
        #     new_user.set_password(password)
        #     new_user.save()

        #     return redirect('sign_in')

    context = {
        'form': form
    }
    return render(request, 'users/sign_up.html', context)


def sign_in(request):
    form = SignInForm()
    user = None
    if request.method == 'POST':
        form = SignInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # LOGIN WITH USERNAME OR EMAIL
            user = User.objects.get(
                Q(username=username) | Q(email=username))

            user = authenticate(username=user.username, password=password)
            # user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {
        'form': form
    }
    return render(request, 'users/sign_in.html', context)


@login_required
def sign_out(request):
    logout(request)
    return redirect('sign_in')
