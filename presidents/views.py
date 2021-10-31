from django.shortcuts import render, get_object_or_404
from .models import President, Party


def about(request, president_id):
    president = get_object_or_404(President, pk=president_id)
    context = {'president': president}
    return render(request, 'presidents/about.html', context)

def index(request):
    pass

def party(request):
    pass

# Create your views here.
