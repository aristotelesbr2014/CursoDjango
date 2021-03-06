from django.db import models

# Create your models here.
class Regiao(models.Model):
	# Validação de unicidade
	nome = models.CharField(max_length = 32, unique = True, verbose_name = "Nome")
	sigla = models.CharField(max_length = 2, unique = True, verbose_name = "Sigla")

	class Meta:
		verbose_name = "Região"
		verbose_name_plural = "Regiões"
		# Altera o nome da tabela
		# db_table = "Novo nome para tabela"

	def __str__(self):
		return "{n}({s})".format(n = self.nome, s = self.sigla)


class Estado(models.Model):
	"""docstring for Estado"""
	nome = models.CharField(max_length = 32, unique = True)
	sigla = models.CharField(max_length = 2, unique = True)
	regiao = models.ForeignKey(Regiao)

	class Meta:
		verbose_name = "Estado"
		verbose_name_plural = "Estados"

	def __str__(self):
		return "{n}".format(n = self.nome)

class Cidade(models.Model):
	"""docstring for Cidade"""
	nome = models.CharField(max_length = 32, unique = True)
	stado = models.ForeignKey(Estado)
	ddd = models.CharField(max_length = 2, verbose_name = "DDD", help_text = "Discagem Direta a Distancia")

	class Meta:
		verbose_name = "Cidade"
		verbose_name_plural = "Cidades"

	def __str__(self):
		return "{n}".format(n = self.nome)
