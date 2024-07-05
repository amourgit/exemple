from django import forms
from .models import StockArticle, CategorieArticle

class ArticleForm(forms.ModelForm):
    id_categorie = forms.ModelChoiceField(queryset = CategorieArticle.objects.all(),
                                            required=True,
                                            label = "Categorie", 
                                            )
    libelle = forms.CharField(required=True,
                            label = "Libelle", 
                            widget = forms.TextInput(attrs={
                                                    'class': 'libelle',
                                                    'type': 'Text',
                                                    'placeholder': "Libelle de l'article",
                                                    }))
    quantite = forms.IntegerField(required=True,
                                label = "Quantite", 
                                )
    
    """description = forms.ChoiceField(required = False,
                                    label = "Description",
                                    widget = forms.Textarea(attrs={
                                                            'class': 'description',
                                                            'type': 'text',
                                                            'placeholder': "description de l'article"
                                                            }))"""
    class Meta:
        model = StockArticle
        fields = [
            'id_categorie',
            'libelle',
            'quantite',
            'description',
        ]