from CNAB_PARSE.serializers import CnabSerializer
from rest_framework.views import APIView, status
from rest_framework.response import Response
from .models import Cnab
from datetime import date, time


def slice_and_generate_list(str_cnab: str):
    init_parse = 0
    end_parse = 80
    listCnab = []
    while (init_parse < len(str_cnab)):
        cnab = str_cnab[init_parse:end_parse]
        dict_cnab = {
            'tipo': cnab[0:1],
            'data': date(int(cnab[1:5]), int(cnab[5:7]), int(cnab[7:9])),
            'valor': (float(cnab[9:19])/100),
            'cpf': cnab[19: 30],
            'cartao': cnab[30: 42],
            'hora': time(int(cnab[42:44]), int(cnab[44:46]), int(cnab[46:48])),
            'dono_da_loja': cnab[48:62].strip(),
            'nome_da_loja': cnab[62:80].strip()
        }
        listCnab.append(dict_cnab)
        init_parse += 80
        end_parse += 80
    return listCnab


class CnabAutoView(APIView):

    def get(self, request):
        cnab_data = Cnab.objects.all().order_by('id')
        serializer = CnabSerializer(cnab_data, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.FILES.get('file', False):
            file_request = request.FILES['file']
        else:
            return Response('algo de errado não está certo', 400)
        file = file_request.read().decode("utf-8").replace('\r\n', '')
        list_cnab = slice_and_generate_list(file)
        serializer = CnabSerializer(data=list_cnab, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)
