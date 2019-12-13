from django.urls import path
from .views import *

urlpatterns = [
    path('', inicial, name='index'),
    path('cursos', listar_cursos, name='listar_cursos'),
    path('cad_curso', cadastrar_curso, name='cad_curso'),
    path('editar_curso/<int:id>', editar_curso, name='editar_curso'),
    path('remover_curso/<int:id>', remover_curso, name='remover_curso'),

    path('instituicoes', listar_instituicoes, name='listar_instituicoes'),
    path('cad_instituicao', cadastrar_instituicao, name='cad_instituicao'),
    path('editar_instituicao/<int:id>', editar_instituicao, name='editar_instituicao'),
    path('remover_instituicao/<int:id>', remover_instituicao, name='remover_instituicao'),

    path('alunos', listar_alunos, name='listar_alunos'),
    path('cad_aluno', cadastrar_aluno, name='cad_aluno'),
    path('editar_aluno/<int:id>', editar_aluno, name='editar_aluno'),
    path('remover_aluno/<int:id>', remover_aluno, name='remover_aluno'),

    path('cad_telefone/<int:id>', cadastrar_telefone, name='cad_telefone'),
    path('editar_telefone/<int:id>', editar_telefone, name='editar_telefone'),
    path('remover_telefone/<int:id>', remover_telefone, name='remover_telefone')
]
