from django.shortcuts import render

# Create your views here.
def perdidos(request):
    return render(request, 'perdidos.html', {})