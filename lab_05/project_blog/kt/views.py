from django.shortcuts import render, redirect, get_object_or_404
from .models import Kontakt
from .forms import KontaktForm


# Create your views here.
def home(request):

    listaKontaktow = Kontakt.objects.all()
    return render(request, "home.html", {"dane": listaKontaktow})


def dodaj(request):

    if request.method == "POST":

        ob = KontaktForm(request.POST)
        ob.save()

        return redirect("home")
    else:
        formularz = KontaktForm()
        return render(request, "dodaj.html", {"formKontakt": formularz})


def edytuj(request, pk):

    obiekt = get_object_or_404(Kontakt, pk=pk)

    if request.method == "POST":

        ob = KontaktForm(request.POST, instance=obiekt)
        if ob.is_valid():
            ob.save()
            return redirect("home")
        else:
            formularz = KontaktForm(instance=obiekt)
            return render(request, "edytuj.html", {"formKontakt": formularz})
    else:
        formularz = KontaktForm(instance=obiekt)
        return render(request, "edytuj.html", {"formKontakt": formularz})


def usun(request, pk):
    Kontakt.objects.filter(pk=pk).delete()
    return redirect("home")
