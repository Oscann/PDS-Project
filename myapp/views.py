from django.shortcuts import render

# Create your views here.
def otavio(request):
    return render(request, 'otavio.html')

def kellyson(request):
    return render(request, 'kellyson.html')