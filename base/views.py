from django.shortcuts import render
from .models import Translator
# Create your views here.
def index(request):
    if request.method == 'GET':
        word = request.GET.get('q', '')
        words = Translator.objects.filter(english__contains=word)
    else:
        words = Translator.objects.all()

    return render(request, 'index.html', {'q': word, 'words': words})
