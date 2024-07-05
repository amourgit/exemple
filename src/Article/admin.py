from django.contrib import admin
from .models import StockArticle, CategorieArticle
from .forms import ArticleForm 

# Register your models here.
@admin.register(StockArticle)
class StockArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    add_form = ArticleForm
    
    list_display = ['libelle', 'id_categorie']
    list_filter = ['id_categorie']
    fieldsets = [
        ("Information de l'article", {'fields': ('id_categorie',
                                                   'libelle',
                                                    'quantite',
                                                    'description'
                                                    )}),
        ("Information du Systeme", {'fields': ('is_deleted', 
                                                 )}),
    ]
    
    add_fieldsets = []
    search_fields = ['libelle']
    ordering = ['id_categorie']
    filter_horizontal = ()


admin.site.register(CategorieArticle)
