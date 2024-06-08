from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request, "novaapp/index.html")

def about_me_view(request):
    return render(request, "novaapp/about_me.html")

def journal_entrances_view(request):
    return render(request, "novaapp/journal_entrances.html")

def media_view(request):
    return render(request, "novaapp/media.html")
