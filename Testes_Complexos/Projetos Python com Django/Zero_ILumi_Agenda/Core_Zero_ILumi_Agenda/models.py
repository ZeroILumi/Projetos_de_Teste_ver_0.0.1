from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_do_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_da_criacao_do_evento = models.DateTimeField(auto_now=True, verbose_name='Data de Criação deste Evento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        db_table = 'Evento'

    def __str__(self):
        return self.titulo