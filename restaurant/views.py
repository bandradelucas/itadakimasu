from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'token': 'teste',
    }
    return render(request, 'restaurant/index.html', context)