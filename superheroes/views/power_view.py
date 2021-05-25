from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from superheroes.forms import PowerForm
from superheroes.models import Powers
from superheroes.models import Powers_character


@login_required
def update(request, id):
    power = Powers.objects.get(id=id)
    form = PowerForm(request.POST or None, instance=power)
    if form.is_valid():
        form.save()
        return redirect("powers")

    context = {
        'form': form
    }
    return render(request, 'power/form_update.html', context)


@login_required
def create(request):
    form = PowerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("powers")

    context = {
        'form': form
    }
    return render(request, 'power/form_save.html', context)


@login_required
def list(request):
    lista = Powers.objects.all()
    character = Powers_character.objects.all()
    return render(request, 'power/index.html', {'powers': lista,'powers_character':character})

@login_required
def delete(request, id):
    power=Powers.objects.get(pk=id)
    power.delete()
    return redirect("powers")
