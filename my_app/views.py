from django.shortcuts import render
import requests

# Create your views here.
def list (request):
	url = "https://pokeapi.co/api/v2/pokemon/"

	nxt = request.GET.get('nextPage')
	prev = request.GET.get('prevPage')

	if nxt:
		print(nxt)
		print(type(nxt))
		response = requests.get(nxt).json()
	elif prev:
		print(prev)
		print(type(prev))
		response = requests.get(prev).json()
	else:
		response = requests.get(url).json()

	context = {
		'response': response,
	}

	return render (request, "list.html", context)

def detail (request):
	url = request.GET.get('detail')
	response = requests.get(url).json()

	context = {
		"results": response,
	}

	return render (request, "detail.html", context)

