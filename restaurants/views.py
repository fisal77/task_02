from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bootcamp77(request):
	context = {
		"msg": "Al-Baik resturant",
		"title": "Spicy checken"
	}
	return render(request, 'albaik.html', context)
