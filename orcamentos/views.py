from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto
from .forms import ProjetoForm

# Create your views here.


def listar_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'orcamentos/listar_projetos.html', {'projetos': projetos})

def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto criado com sucesso!')
            return redirect('listar_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'orcamentos/form_projeto.html', {'form': form, 'titulo': 'Novo Projeto'})

def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Projeto atualizado com sucesso!')
            return redirect('listar_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'orcamentos/form_projeto.html', {'form': form, 'titulo': 'Editar Projeto'})

def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        messages.success(request, 'Projeto excluído com sucesso!')
        return redirect('listar_projetos')
    return render(request, 'orcamentos/confirmar_exclusao_projeto.html', {'projeto': projeto})