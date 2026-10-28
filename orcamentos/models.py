from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    prioridade = models.CharField(
        max_length=20, 
        choices=[('Baixa', 'Baixa'), ('Media', 'Média'), ('Alta', 'Alta')]
    )
    concluido = models.BooleanField(default=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='tarefas')

    def __str__(self):
        return self.titulo
