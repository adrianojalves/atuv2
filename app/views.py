from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def inicial(request):
    return render(request, 'index.html', {})


"""
VIEWS DE CURSOS
"""
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/index.html', {'cursos': cursos})


def cadastrar_curso(request):
    if request.method == "POST":
        form_curso = CursoForm(request.POST)
        if form_curso.is_valid():
            form_curso.save()
            return listar_cursos(request)
    else:
        form_curso = CursoForm()
    return render(request, 'cursos/cad_curso.html', {'form_curso': form_curso})


def editar_curso(request, id):
    curso_bd = Curso.objects.get(id=id)
    form_curso = CursoForm(request.POST or None, instance=curso_bd)

    if form_curso.is_valid():
        form_curso.save()
        return listar_cursos(request)
    return render(request, 'cursos/cad_curso.html', {'form_curso': form_curso})


def remover_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        return listar_cursos(request)
    return render(request, 'cursos/confirma_exclusao.html', {'curso': curso})
"""
FIM VIEWS DE CURSOS
"""


"""
VIEWS DE INSTITUIÇÕES DE ENSINO
"""
def listar_instituicoes(request):
    instituicoes = InstituicaoEnsino.objects.all()
    return render(request, 'instituicoes/index.html', {'instituicoes': instituicoes})


def cadastrar_instituicao(request):
    if request.method == "POST":
        form_instituicao = InstituicaoForm(request.POST)
        if form_instituicao.is_valid():
            form_instituicao.save()
            return listar_instituicoes(request)
    else:
        form_instituicao = InstituicaoForm()
    return render(request, 'instituicoes/cad_instituicao.html', {'form_instituicao': form_instituicao})


def editar_instituicao(request, id):
    instituicao_bd = InstituicaoEnsino.objects.get(id=id)
    form_instituicao = InstituicaoForm(request.POST or None, instance=instituicao_bd)

    if form_instituicao.is_valid():
        form_instituicao.save()
        return listar_instituicoes(request)
    return render(request, 'instituicoes/cad_instituicao.html', {'form_instituicao': form_instituicao})


def remover_instituicao(request, id):
    instituicao = InstituicaoEnsino.objects.get(id=id)
    if request.method == "POST":
        instituicao.delete()
        return listar_instituicoes(request)
    return render(request, 'instituicoes/confirma_exclusao.html', {'instituicao': instituicao})
"""
FIM VIEWS DE INSTITUIÇÕES DE ENSINO
"""

"""
VIEWS DE ALUNOS
"""
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/index.html', {'alunos': alunos})


def cadastrar_aluno(request):
    if request.method == "POST":
        form_aluno = AlunoForm(request.POST)
        if form_aluno.is_valid():
            aluno = form_aluno.save()
            return redirect('editar_aluno', aluno.id)
    else:
        form_aluno = AlunoForm()
    return render(request, 'alunos/cad_aluno.html', {'form_aluno': form_aluno, 'telefones': [], 'update': False, 'cod_aluno': 0})


def editar_aluno(request, id, valida_form = True):
    aluno_bd = Aluno.objects.get(id=id)

    if valida_form:
        form_aluno = AlunoForm(request.POST or None, instance=aluno_bd)
    else:
        form_aluno = AlunoForm(None, instance=aluno_bd)

    if form_aluno.is_valid():
        form_aluno.save()
        return listar_alunos(request)

    telefones = TelefoneAluno.objects.filter(cod_aluno=id)
    return render(request, 'alunos/cad_aluno.html', {'form_aluno': form_aluno, 'telefones': telefones, 'update': True, 'cod_aluno': id})


def remover_aluno(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method == "POST":
        aluno.delete()
        return listar_alunos(request)
    return render(request, 'alunos/confirma_exclusao.html', {'aluno': aluno})
"""
FIM VIEWS DE ALUNOS
"""

"""
VIEWS DE TELEFONE ALUNO
"""
def cadastrar_telefone(request, id):
    if request.method == "POST":
        form_telefone = TelefoneAlunoForm(request.POST)
        if form_telefone.is_valid():
            telefone = form_telefone.cleaned_data["telefone"]
            cod_aluno = request.POST['cod_aluno']
            aluno = Aluno.objects.get(id=cod_aluno)
            tel = TelefoneAluno()
            tel.cod_aluno = aluno
            tel.telefone = telefone
            tel.save()
            request.method = None
            return redirect('editar_aluno', cod_aluno)
    else:
        form_telefone = TelefoneAlunoForm()
        form_telefone.Meta.model.cod_aluno_id = id
        aluno = Aluno.objects.get(id=id)
        return render(request, 'alunos/cad_telefone.html', {'form_telefone': form_telefone, 'aluno': aluno})


def editar_telefone(request, id):
    tel_bd = TelefoneAluno.objects.get(id=id)
    cod = tel_bd.cod_aluno
    form_telefone = TelefoneAlunoForm(request.POST or None, instance=tel_bd)

    if form_telefone.is_valid():
        telefone = form_telefone.cleaned_data["telefone"]
        cod_aluno = request.POST['cod_aluno']
        aluno = Aluno.objects.get(id=cod_aluno)
        tel = TelefoneAluno()
        tel.id = id
        tel.cod_aluno = aluno
        tel.telefone = telefone
        tel.save()
        #return editar_aluno(request, cod_aluno, False)
        print('VAI REDIRECIONAR')
        return redirect('editar_aluno', cod_aluno)

    return render(request, 'alunos/cad_telefone.html', {'form_telefone': form_telefone, 'aluno': tel_bd.cod_aluno})

def remover_telefone(request, id):
    telefone = TelefoneAluno.objects.get(id=id)
    cod_aluno = telefone.cod_aluno.id
    telefone.delete()
    return redirect('editar_aluno', cod_aluno)