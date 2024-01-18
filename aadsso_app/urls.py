from aadsso_app.views import index 
from django.urls import path ,include
from django.contrib import admin 
# from .views import signup
urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', index),
    path("", include("webUI.urls")),

]
