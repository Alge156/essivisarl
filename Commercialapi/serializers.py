from rest_framework.serializers import ModelSerializer
from .models import Commercial
from .models import Client
from .models import Depot
from .models import Produit
from .models import Commande


class CommercialSerializer(ModelSerializer):
    class Meta:
        model=Commercial
        fields=['id','nom','prenom', 'numero']

class ClientSerializer(ModelSerializer):
    class Meta:
        model=Client
        fields=['id','nom','prenom','numero']

class DepotSerializer(ModelSerializer):
    class Meta:
        model=Depot
        fields=['id','quantite','heure'] 



class ProduitSerializer(ModelSerializer):
    class Meta:
        model=Produit
        fields=['id','nom','prix'] 


class CommandeSerializer(ModelSerializer):
    class Meta:
        model=Commande
        fields=['id','client','produit'] 