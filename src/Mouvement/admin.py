from django.contrib import admin
from .models import Mouvement
from .forms import MouvementForm
# Register your models here.


@admin.register(Mouvement)
class MouvementAdmin(admin.ModelAdmin):
    form = MouvementForm
    add_form = MouvementForm
    
    list_display = ['visible', 'type_mouvement', 'id_article', 'id_user', 'quantite']
    list_filter = ['type_mouvement', 'visible', 'id_user', 'id_article']
    fieldsets = [
        ("Information du Mouvement", {'fields': ('type_mouvement',
                                                   'id_article',
                                                    'quantite',
                                                    'id_user',
                                                    'motif'
                                                    )}),
        ("Information du Systeme", {'fields': ('visible', 
                                                 )}),
    ]
    
    add_fieldsets = []
    search_fields = ['id_user', 'id_article']
    ordering = ['type_mouvement']
    filter_horizontal = ()
