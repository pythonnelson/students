from django.shortcuts import render
from students.models import *

def dashboard(request):
	return render(request, "dashboard.html")