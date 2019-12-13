from django.db import models

class Aluno(models.Model):
    cpf = models.CharField(max_length=14, null=False, blank=False, unique=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    rg = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=100, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False, default="av")

    def __str__(self):
        return self.nome


class TelefoneAluno(models.Model):
    cod_aluno = models.ForeignKey("Aluno", on_delete=models.CASCADE, null=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)


class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    rua = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=20, null=False, blank=False)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=20, null=False, blank=False)
    cep = models.CharField(max_length=8, null=False, blank=False)

    def __str__(self):
        return self.nome


class Curso(models.Model):
    TIPOS_CHOICE = [
        (1, "Fundamental"),
        (2, "Médio"),
        (3, "Superior"),
        (4, "Técnico"),
        (5, "Profissional")
    ]

    TURNOS_CHOICE = [
        (1, "Matutino"),
        (2, "Vespertino"),
        (3, "Noturno"),
        (4, "Integral")
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    tipo = models.IntegerField(choices=TIPOS_CHOICE, null=False, blank=False)
    turno = models.IntegerField(choices=TURNOS_CHOICE, null=False, blank=False)

    def __str__(self):
        return self.nome
