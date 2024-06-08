from django.contrib import admin
from .models import Praia
from .models import Regiao
from.models import Servico

# Register your models here.


class PraiaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('nome',)
    search_fields = ('nome',)

class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('nome_regiao',)
    ordering = ('nome_regiao',)
    search_fields = ('nome_regiao',)

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome_servico',)
    ordering = ('nome_servico',)
    search_fields = ('nome_servico',)

admin.site.register(Praia, PraiaAdmin)
admin.site.register(Regiao, RegiaoAdmin)
admin.site.register(Servico, ServicoAdmin)