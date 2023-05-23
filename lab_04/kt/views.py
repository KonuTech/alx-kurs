from django.shortcuts import render
from .models import Kontakt

# Create your views here.
def home(request):

    listaKontaktow = Kontakt.objects.all()
    return render(request, "home.html", {"dane":listaKontaktow})