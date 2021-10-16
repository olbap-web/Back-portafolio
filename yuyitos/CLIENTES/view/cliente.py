from django.shortcuts import render

from rest_framework.views import APIView


from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework import status
from rest_framework.response import Response

#models
from CLIENTES.model.cliente import Cliente
from CLIENTES.model.cliente import ClienteSerializer

class IndexPageView(APIView):


    def get(self, request, *args, **kwargs):
        try:
            cli = Cliente.objects.all()
            serial = ClienteSerializer(cli, many=True)

        except Exception as ex:
            print(str(ex), ': error try get toda las solicitudes')

        return JsonResponse(serial.data, safe=False)
    
    def post(self, request,*args, **kwargs):

        seriaCli = ClienteSerializer(data= request.data)
        if seriaCli.is_valid():
            seriaCli.save()
            return Response(seriaCli.data, status=status.HTTP_201_CREATED)
        return Response(seriaCli.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteView(APIView):

    def get(self,request, *args, **kwargs):
        
        try:
            cliente = Cliente.objects.get(pk=self.kwargs['pk'])
        
        except Exception as ex:
            print(str(ex), 'try_:_:')
        
        serialCliente = ClienteSerializer(cliente)

        return JsonResponse(serialCliente.data)
    
