"""
URL configuration for aadsso project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from webUI.views import (
    login_view,
    dashboard,
    # entra_access,
    logout_view
)
from entra_auth.views import (
    microsoft_login,
    microsoft_logout,
    callback,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    # path('entra_auth/', include('entra_auth.urls')),
    # path('entra_access/', entra_access, name='entra_access'),
    path('entra_auth/login', microsoft_login, name="entra_auth_login"),
    path('entra_auth/logout', microsoft_logout, name="entra_auth_logout"),
    path('entra_auth/callback', callback, name="entra_auth_callback"),
    path('logout/', logout_view, name='logout'),
]
