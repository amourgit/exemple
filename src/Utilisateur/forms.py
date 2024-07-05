from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as Auth_form
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from Article.models import StockArticle
User = get_user_model()
  
    
 
class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirmation du password',  widget=forms.PasswordInput)
    genre = forms.ChoiceField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')],
                            label = "Genre")
    class Meta:
        model = User
        fields = ['username', 'password_2', 'genre']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password_2')
        if password is not None and password !=  password_2:
            self.add_error("password_2", "Your password must match")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    genre = forms.ChoiceField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')],
                            label = "Genre")
    class Meta:
        model = User
        fields = ['username', 'genre']
    
    def clean_password(self):
        return self.initial["password"]

    



class UserForm(forms.ModelForm):
    
    nom = forms.CharField(required=True,
                            label = "Nom(s)", 
                            widget = forms.TextInput(attrs={
                                                    'class': 'nom',
                                                    'type': 'Text',
                                                    'placeholder': "Votre Nom"
                                                    }))
    prenom = forms.CharField(required=True,
                            label = "Prenom(s)", 
                            widget = forms.TextInput(attrs={
                                                    'class': 'prenom',
                                                    'type': 'Text',
                                                    'placeholder': "Votre Prenom"
                                                    }))
    contact = forms.CharField(required=True,
                            label = "Contact", 
                            widget = forms.TextInput(attrs={
                                                    'class': 'contact',
                                                    'type': 'Text',
                                                    'placeholder': "ex : +241 65 xx xx xx"
                                                    }))
    genre = forms.ChoiceField(choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')],
                            label = "Genre",
                            )
    email = forms.CharField(required=True,
                            label = "Email", 
                            widget = forms.TextInput(attrs={
                                                    'class': 'email',
                                                    'type': 'email',
                                                    'placeholder': " ex: exemple@gmail.com"
                                                    }))
    
    class Meta:
        model = User
        fields = [
            'nom',
            'prenom',
            'contact',
            'genre',
            'email',
        ]
    
