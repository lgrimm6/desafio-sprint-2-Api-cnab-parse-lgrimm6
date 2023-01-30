from rest_framework import serializers

from .models import Cnab


class CnabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnab
        fields = ['id',
                  'tipo',
                  'data',
                  'valor',
                  'cpf',
                  'cartao',
                  'hora',
                  'dono_da_loja',
                  'nome_da_loja']
