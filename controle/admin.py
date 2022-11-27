from django.contrib import admin
from .models import Produtos
from .models import Tabela
from .models import transacao
from .models import Estoque


admin.site.register(Produtos)
admin.site.register(Tabela)
admin.site.register(transacao)
admin.site.register(Estoque)
