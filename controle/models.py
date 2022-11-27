from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Tabela(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)


class transacao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    descrição = models.CharField(max_length=100)

    def __str__(self):
        return self.descrição


class Estoque(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descricao

