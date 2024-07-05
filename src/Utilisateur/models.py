from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, AbstractUser, PermissionsMixin, Group, Permission
)
from django.core.mail import send_mail

"""
class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Les Utilisateurs doivent avoir un nom utilisateur')
        #user = self.model(username=self.normalize_username(username),)
        user = self.model(username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_staffuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username,
            password=password,
        )
        user.is_superuser = True
        user.is_active = True
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

"""


class User(AbstractUser, PermissionsMixin):
    ### Informations Personnelles
    nom = models.CharField(max_length=100, blank = True, null = True)
    prenom = models.CharField(max_length=100, blank = True, null = True)
    contact = models.CharField(max_length=100, unique=True, blank = True, null = True)
    genre = models.CharField(max_length=100, blank = True, null = True)
    email = models.EmailField(max_length=100, blank = True, null = True)

    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = "Utilisateurs"
        verbose_name = "Utilisateur"




class TypeUtilisateur(models.Model):
    type_user =  models.CharField(max_length=255, blank=True, verbose_name="Type d'Utilisateur")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Creation') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
    
    class Meta:
        verbose_name_plural = "Types Utilisateur"
        verbose_name = "Type"
    
    def __str__(self) ->str:
        return self.type_user