from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from superheroes.models import Character
from superheroes.forms import CharacterForm
from superheroes.forms import Powers_character
from django.http import HttpResponse


def listPrincipal(request):
    lista = Powers_character.objects.filter(number='82')
    return render(request, 'principal\index.html', {'characters': lista})


def list(request):
    lista = Character.objects.all()
    return render(request, 'character\index.html', {'characters': lista})


def detail(request, id):
    character = Character.objects.get(id=id)
    data_power = Powers_character.objects.all().filter(character_id=id)
    return render(request, 'character\detail.html', {'character': character, 'powers': data_power})


def search(request):
    search = request.POST.get('search', False)
    filter = Character.objects.filter(name__startswith=search)
    return render(request, 'character\search.html', {'character': filter})


def search_universe(request):
    search = request.POST.get('search', False)
    filter = Character.objects.filter(universe_id__name__startswith=search)
    return render(request, 'character\search_universe.html', {'character': filter})


def search_power(request):
    search = request.POST.get('search', False)
    filter = Powers_character.objects.filter(powers_id__name__startswith=search)
    return render(request, 'character\search_power.html', {'character': filter})


@login_required
def update(request, id):
    character = Character.objects.get(id=id)
    form = CharacterForm(request.POST or None, instance=character)
    if form.is_valid():
        form.save()
        return redirect("characters")
    context = {
        'form': form
    }
    return render(request, "character/form_update.html", context)


@login_required
def create(request):
    form = CharacterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("characters")

    context = {
        'form': form

    }

    return render(request, "character/form_save.html", context)


@login_required
def delete(request, id):
    character = Character.objects.get(pk=id)
    character.delete()
    return redirect("characters")
