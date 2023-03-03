from django.db import models

# Create your models here.
class Commercial(models.Model):
    nom= models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    numero=models.IntegerField()

    def __str__(self):
        return self.nom +''+ self.prenom +''+ self.numero
    

class Client(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    numero=models.IntegerField()
    

    def __str__(self):
        return self.nom +''+ self.prenom +''+ self.numero
    
class Depot(models.Model):
    quantite=models.IntegerField()
    heure=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.quantite+''+self.heure  


class Produit(models.Model):
    nom=models.CharField(max_length=100)
    prix=models.IntegerField()

    def __str__(self):
        return self.nom+''+self.prix
    

class Commande(models.Model):
    client=models.ForeignKey(Client,null=True, on_delete=models.SET_NULL)
    produit=models.ForeignKey(Produit,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.client+''+self.produit



