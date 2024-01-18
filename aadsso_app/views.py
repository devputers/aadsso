from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from entra_auth.auth.auth_decorators import (
    microsoft_login_required, login_required_with_AD
)
from django.conf import settings
from django.http import HttpResponseRedirect
from entra_auth.views import microsoft_logout


def loginpublic_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        print("user",user)
        
        # if user is not None:
        if user is not None:

            login(request, user)
            # return redirect('dashboard')  # Redirect to a dashboard page
            # return redirect(request.GET.get('next', 'dashboard'))\
            return render(request, 'dashboard.html', {'user':
                                                  user})
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message':
                                                  error_message})
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'login.html')


# way 2
# _________
# @login_required()
# def dashboard(request):
#     return render(request, 'dashboard.html')


# @microsoft_login_required(groups=("mssso",)) # must be group
# def entra_access(request):
#     return render(request, 'dashboard.html')
# __________

# way 1
# __________
@login_required_with_AD
def dashboard(request):
    return render(request, 'dashboard.html')
# __________

def logout_view(request):
    from django.shortcuts import redirect
    from django.contrib.auth import logout
    microsoft_logout(request)
    logout(request)
    return redirect('login')