from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.


class PoA(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)
    identidade = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __string__(self):
        return self.nome

    # mandar os kwargs por baixo dos panos
    def get_absolute_url(self):
        return reverse('poa:detail', kwargs={'nome': self.nome, 'pk': self.pk})
