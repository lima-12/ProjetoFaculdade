from django.contrib import admin
from .models import Produtos
from .models import Tabela
from .models import transacao


admin.site.register(Produtos)
admin.site.register(Tabela)
admin.site.register(transacao)
