from django.contrib import admin
from . models import Fabricante, Marca, Produto, Categoria, Lote, Prateleira, Estoque

# INLINES
class MarcaInline(admin.StackedInline):
	model = Marca
	extra = 1


class ProdutoInline(admin.StackedInline):
	model = Produto
	extra = 1


# MODEL ADMIN
class FabricanteAdmin(admin.ModelAdmin):
	# Formata as tabelas de exibição.
	list_display = ('nome', 'endereco', 'cidade', 'cnpj')
	# Gera o nestendForm
	inlines = [
		MarcaInline,
	]


class MarcaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'fabricante')
	list_filter = ('fabricante',)
	inlines = [
		ProdutoInline,
	]


class ProdutoAdmin(admin.ModelAdmin):
	# "marca__fabibricante" Busca todos as marcas atraves do fabricante
	list_filter = ('marca', 'marca__fabricante', 'categoria')
	list_display = ('nome', 'marca', 'codigo', 'categoria')
	search_fields = ['codigo', 'nome']


admin.site.register(Fabricante, FabricanteAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
admin.site.register(Lote)
admin.site.register(Prateleira)
admin.site.register(Estoque)
