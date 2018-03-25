from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def fencing(request):
    return fencing_history(request)


def fencing_history(request):
    return render(request, 'fencing_history.html')


def fencing_events(request):
    return render(request, 'fencing_events.html')


def fencing_club(request):
    return render(request, 'fencing_club.html')


def contact(request):
    return render(request, 'contact.html')