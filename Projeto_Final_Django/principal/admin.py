from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Estado)
# admin.site.register(Cidade)
# admin.site.register(Bairro)
# -- Requerente --
admin.site.register(CPF)
admin.site.register(EnderecoRequerente)
admin.site.register(Requerente)

# -- Serviços --
admin.site.register(EnderecoObra)
admin.site.register(ResponsavelTecnico)
admin.site.register(AlvaraConstrucao)