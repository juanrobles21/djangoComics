from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def loginView(request):
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(request, username=_username, password=_password)
        print(user)

        if user:
            login(request, user)
            return redirect("UniverseComics")
        else:
            return render(request, 'users/login.html', {'error': 'el usuario no se encuentra registrado'})

    return render(request, 'users/login.html')


@login_required
def logout_v(request):
    logout(request)
    return redirect("UniverseComics")
    #return render(request, 'users/login.html')
