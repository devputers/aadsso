from django.urls import path
from entra_auth.views import (
    microsoft_login,
    microsoft_logout,
    callback,
)

app_name = 'entra_auth'
urlpatterns = [
    path('login', microsoft_login, name="entra_auth_login"),
    path('logout', microsoft_logout, name="entra_auth_logout"),
    path('callback', callback, name="entra_auth_callback"),
]
