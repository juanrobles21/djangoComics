from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from superheroes.models import Powers_character
from superheroes.forms import powerCharacterForm


@login_required
def create(request):
    form = powerCharacterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("powers")

    context = {
        'form': form

    }

    return render(request, 'powers_character/form_power_character.html', context)


@login_required
def update(request, id):
    power_character = Powers_character.objects.get(id=id)
    form = powerCharacterForm(request.POST or None, instance=power_character)
    if form.is_valid():
        form.save()
        return redirect("powers")
    context = {
        'form': form
    }
    return render(request, 'powers_character/form_update.html', context)


@login_required
def delete(request,id):
    power_character=Powers_character.objects.get(pk=id)
    power_character.delete()
    return redirect("powers")
