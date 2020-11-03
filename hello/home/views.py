from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':"this is sent"
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse('Thiis page is about the webdevelopment')

def pic(request):
    return HttpResponse('Return Picture')

def feedback(request):
    return render(request, 'feedback.html')
