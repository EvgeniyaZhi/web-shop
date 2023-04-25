from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_up.html', context={
            'title': 'Реєстрація',
            'page': 'sign_up',
            'app': 'accounts'
        })
    else:
        # 1
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')
        email_x = request.POST.get('email')

        # 2
        user = User.objects.create_user(login_x, email_x, pass1_x)
        user.save()

        # 3
        if user is None:
            color = 'red'
            message = 'В реєстрації відмовлено!'
        else:
            color = 'green'
            message = 'Реєстрація успішно завершена!'

        # 4
        return render(request, 'accounts/reports.html', context={
            'title': 'Звіт про реєстрацію',
            'page': 'reports',
            'app': 'accounts',
            'color': color,
            'message': message
        })


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/sign_in.html', context={
            'title': 'Авторизація',
            'page': 'sign_in',
            'app': 'accounts'
        })
    else:
        # 1
        login_x = request.POST.get('login')
        pass1_x = request.POST.get('pass1')

        # 2
        user = authenticate(request, username=login_x, password=pass1_x)

        # 3
        if user is None:
            color = 'red'
            message = 'Користувач не знайдений!'
        else:
            login(request, user)
            return redirect('/')

        # 4
        return render(request, 'accounts/reports.html', context={
            'title': 'Звіт про авторизацію',
            'page': 'reports',
            'app': 'accounts',
            'color': color,
            'message': message
        })


def sign_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль',
        'page': 'profile',
        'app': 'accounts'
    })
