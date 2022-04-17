from django.contrib import admin
from django.urls import path, include
from . views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('students/', include('students.urls', namespace='students')),
]
