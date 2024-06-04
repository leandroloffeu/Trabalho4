from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento
from .forms import EventoForm

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'evento/lista_eventos.html', {'evento': eventos})

def criar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'evento/form_evento.html', {'form': form})

def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'evento/form_evento.html', {'form': form})

def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    evento.delete()
    return redirect('lista_eventos')

