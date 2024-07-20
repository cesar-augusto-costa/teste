from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "todos/home.html")


# A funcao a seguir será trocada por uma Class Based View
"""
def todoListar(request):
    # tarefas = [{
    #     'id':'1',
    #     'Tarefa':'comprar fraldas'
    # }]
    tarefas = Todo.objects.all()  # busca todos os dados do banco
    return render(request, "todos/todolistar.html",{'tarefas':tarefas})
"""


class todoListarView(ListView):
    model = Todo  # classe deve usar o modelo ToDo (.\todos\models.py)

class todoCriarView(CreateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]  # Uma lista de campos que o usuario pode alterar
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Adicionar Tarefa'
        return context

class todoAtualizarView(UpdateView):
    model = Todo
    fields = ["titulo","dtFinalizado"]
    success_url = reverse_lazy('todo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'Atualizar Tarefa'
        return context

class todoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo_listar')
    template_name = "todos/todo_confirm_dele.html"