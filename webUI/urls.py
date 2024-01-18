# from app.views import index 
from django.urls import path 
from django.contrib import admin 
# from .views import signup
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
