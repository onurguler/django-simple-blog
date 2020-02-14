from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



def user_login(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('index'))

        context['message'] = 'Invalid credentials'

    return render(request, 'users/login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('index'))
