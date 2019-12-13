from django import forms
from .models import *
from django_localflavor_br.forms import BRCNPJField, BRCPFField


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class InstituicaoForm(forms.ModelForm):
    cnpj = BRCNPJField(label='CNPJ', required=True)

    class Meta:
        model = InstituicaoEnsino
        fields = '__all__'


class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'


class TelefoneAlunoForm(forms.ModelForm):

    class Meta:
        model = TelefoneAluno
        fields = fields = ['telefone']
