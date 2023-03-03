from django.db import models


# Create your models here.

class UtilisateurManager(models.Manager):
    
    def get_by_natural_key(self, username):
        return self.get(username=username)











class Utilisateur(models.Model):
    username=models.CharField(max_length=200, unique=True)
    password=models.CharField(max_length=200)
    
    
    objects = UtilisateurManager()


    def set_password(self, password):
        self.password = password

    @property
    def is_anonymous(self):
            return False
        
    @property
    def is_authenticated(self):
            return True


    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD = 'username'




