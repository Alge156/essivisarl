from django.shortcuts import render
from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Commercial
from .models import Client
from .serializers import CommercialSerializer
from .serializers import ClientSerializer
from .models import Depot
from .serializers import DepotSerializer
from .models import Produit
from .serializers import ProduitSerializer
from .models import Commande
from .serializers import CommandeSerializer
# from rest_framework.decorators import api_view
# from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class CommercialAPIViewset(ModelViewSet):
        serializer_class = CommercialSerializer


        def get_queryset(self):
            # categories=Categorie.objects.all()
            # serializer=CategorieSerializer(categories, many=True)
            return Commercial.objects.all()
        

class ClientAPIviewset(ModelViewSet):
      serializer_class=ClientSerializer

      def get_queryset(self):
            return Client.objects.all()
      

class DepotAPIviewset(ModelViewSet):
      serializer_class=DepotSerializer

      def get_queryset(self):
            return Depot.objects.all()      
     
        

class ProduitAPIviewset(ModelViewSet):
      serializer_class=ProduitSerializer

      def get_queryset(self):
            return Produit.objects.all()


class CommandeAPIviewset(ModelViewSet):
      serializer_class=CommandeSerializer

      def get_queryset(self):
            return Commande.objects.all()        
        
        
       