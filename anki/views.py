from django.shortcuts import render

# Create your views here.
def anki(request):
    return render(request,'anki/anki.html')