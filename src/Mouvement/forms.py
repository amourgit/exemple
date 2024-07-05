from django import forms
from .models import Mouvement
from Article.models import StockArticle
from django.contrib.auth import get_user_model
User = get_user_model()


class MouvementForm(forms.ModelForm):
    type_mouvement = forms.ChoiceField(choices=[('Entree', 'Entree'), ('Sortie', 'Sortie')],
                                            required=True,
                                            label = "Type de Mouvement", 
                                            )
    """id_article = forms.ModelChoiceField(queryset = StockArticle.objects.all(),
                                            required=True,
                                            label = "Libelle de l'Article", 
                                            )"""
    quantite = forms.IntegerField(required=True,
                                  initial= 1,
                                label = "Quantite", 
                                )
    
    """id_user = forms.ModelChoiceField(queryset = User.objects.all(),
                                            required=True,
                                            label = "Auteur", 
                                            )"""
    
    """motif = forms.ChoiceField(required = False,
                                    label = "Motif",
                                    widget = forms.Textarea(attrs={
                                                            'class': 'motif',
                                                            'type': 'text',
                                                            'placeholder': "Motif du mouvement..."
                                                            }))"""
    class Meta:
        model = Mouvement
        fields = [
            'type_mouvement',
            'id_article',
            'quantite',
            'id_user',
            'motif',
        ]