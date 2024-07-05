from django.db import models
from Article.models import StockArticle
from django.contrib.auth import get_user_model
User = get_user_model()   

# Create your models here.
class Mouvement(models.Model):
    type_mouvement =  models.CharField(max_length=255, blank=True, verbose_name="Type de Mouvement")
    id_article = models.ForeignKey(StockArticle, blank=True, verbose_name='Article', on_delete=models.CASCADE, null=True)
    quantite  = models.IntegerField(null=True, blank=True, verbose_name="Quantite")
    id_user = models.ForeignKey(User, blank=True, verbose_name='Utilisateur', on_delete=models.CASCADE, null=True)
    motif = models.TextField(max_length=1000, blank=True, null=True, verbose_name="Motif")
    visible = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Creation') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')

    
    class Meta:
        verbose_name_plural = "Mouvements"
        verbose_name = "Mouvement"
    
    def __str__(self) ->str:
        return self.type_mouvement