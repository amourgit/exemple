from django.db import models



class CategorieArticle(models.Model):
    categorie =  models.CharField(max_length=255, blank=True, verbose_name='Categorie')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Creation') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
    
    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Categorie"
    
    def __str__(self) ->str:
        return self.categorie
    

class StockArticle(models.Model):
    id_categorie =  models.ForeignKey(CategorieArticle, blank=True, verbose_name='Categorie', on_delete=models.CASCADE)
    libelle =  models.CharField(max_length=255, blank=True, verbose_name='Libelle')
    quantite =  models.IntegerField(blank=True, verbose_name='Quantite', default=0)
    description =  models.TextField(max_length=1000, blank=True, verbose_name='Description')
    is_deleted = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de Creation') 
    date_updated = models.DateTimeField(auto_now=True, verbose_name='Date de Modification')
    
    class Meta:
        verbose_name_plural = "Articles"
        verbose_name = "Article"
        
    def __str__(self) ->str:
        return self.libelle