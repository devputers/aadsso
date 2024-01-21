from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from entra_auth.auth.auth_decorators import (
    microsoft_login_required, login_required_with_AD
)
from django.conf import settings
from django.http import HttpResponseRedirect
from entra_auth.views import microsoft_logout
from .models import User


def login_view(request):
    c_tenant= request.tenant
    print("c_tenat",c_tenant)
    # settings.ENTRA_CREDS["redirect"] = f"http://{c_tenant}.localhost:8080/entra_auth/callback"
    # settings.ENTRA_CREDS["logout_uri"] = f"http://{c_tenant}.localhost:8080/admin/logout"
        
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # user = authenticate(request, username=username, password=password)
        try:
            user = User.objects.get(username=username)
            if user is not None:
                # login(request, user)
                if user.password == password :
                    request.session['user_login']=True
                    user_data = {'id_user': user.id, 'name_user': user.username}
                    user_data = request.session['user_data'] = user_data
                    # return redirect('dashboard')  # Redirect to a dashboard page
                    # return redirect(request.GET.get('next', 'dashboard'))
                    return render(request, 'dashboard.html', {'user': user_data})
                else:
                    error_message = "Invalid username or password"
                    return render(request, 'login.html', {'error_message':
                                                    error_message})
        except Exception:
                return render(request, 'login.html', {'error_message': 'User does not exist'})
        
    # if request.user.is_authenticated:
        
    login_check = request.session.get('user_login')
    user_data = request.session.get('user_data')
    if login_check : 
        return render(request, 'dashboard.html', {'user': user_data})
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

# def logout_view_local(request):
#     return redirect('login')
