from django.forms import ModelForm
from .models import Estoque


class transacaoForm(ModelForm):
    class Meta:
        model = Estoque
        fields = ['descricao', 'quantidade', 'valor']