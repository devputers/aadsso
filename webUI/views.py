from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return redirect('dashboard')  # Redirect to a dashboard page
            return redirect(request.GET.get('next', 'dashboard'))
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message':
                                                  error_message})

    return render(request, 'login.html')


@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')
