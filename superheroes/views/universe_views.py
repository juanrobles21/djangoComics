from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from superheroes.models import Universe
from superheroes.models import Character
from superheroes.forms import UniverseForm


def list(request):
    lista = Universe.objects.all()
    return render(request, 'universe\index.html', {'universes': lista})


def detail(request, id):
    detail = Universe.objects.get(pk=id)
    filter = Character.objects.filter(universe_id__name=detail)
    return render(request, 'universe\detail.html', {'detail':detail,'characters': filter})


@login_required
def update(request, id):
    universe = Universe.objects.get(id=id)
    form = UniverseForm(request.POST or None, instance=universe)
    if form.is_valid():
        form.save()
        return redirect("universes")
    contex = {
        'form': form
    }
    return render(request, "universe/form_update.html", contex)


@login_required
def create(request):
    form = UniverseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("universes")

    context = {
        'form': form
    }
    return render(request, "universe/create_universe.html", context)


@login_required
def delete(request, id):
    character = Universe.objects.get(pk=id)
    character.delete()
    # return HttpResponse('ok')
    return redirect("universes")
