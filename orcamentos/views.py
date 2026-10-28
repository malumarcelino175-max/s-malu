from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Projeto, Tarefa
from .forms import ProjetoForm, TarefaForm

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

def listar_tarefas(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'orcamentos/listar_tarefas.html', {'tarefas': tarefas})

def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm()
    return render(request, 'orcamentos/form_tarefa.html', {'form': form, 'titulo': 'Nova Tarefa'})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('listar_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'orcamentos/form_tarefa.html', {'form': form, 'titulo': 'Editar Tarefa'})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso!')
        return redirect('listar_tarefas')
    return render(request, 'orcamentos/confirmar_exclusao_tarefa.html', {'tarefa': tarefa})
