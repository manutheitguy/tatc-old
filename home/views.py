from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, 'home/index.html')

def about(request):

    return render(request, 'home/about.html')

def services(request):

    return render(request, 'home/services.html')

def blog(request):

    return render(request, 'home/blog.html', {
    'title': 'Latest Posts'
})