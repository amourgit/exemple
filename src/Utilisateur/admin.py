from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
#from .models import User as user
#from .forms import UserCreationForm, UserChangeForm
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['username', 'nom', 'prenom']
    list_filter = ['username', 'groups']
    fieldsets = (
        ('Information de Connexion', {'fields': ('username', 'password')}),
        ('Information Personnelle', {'fields': (
                                        'nom',
                                        'prenom',
                                        'contact',
                                        'genre',
                                        'email',
                                        )}),
        ('Permissions', {'fields': (
                            'is_active',
                            'is_staff',
                            'is_superuser',
                            'is_deleted',
                            )}),
        ('Permissions Supplementaire', {'fields': ('groups',
                                                'user_permissions',
                                                    )}),
    )
    add_fieldsets = (
        ('Information de Connexion', {'fields': ('username', 'password', 'password_2', )}),
        ('Information Personnelle', {'fields': (
                                        'nom',
                                        'prenom',
                                        'contact',
                                        'genre',
                                        'email',
                                        )}),
        ('Permissions', {'fields': (
                            'is_active',
                            'is_staff',
                            'is_superuser',
                            'is_deleted',
                            )}),
        ('Permissions Supplementaire', {'fields': ('groups',
                                                'user_permissions',
                                                    )}),
    )
    
    search_fields = ['username']
    ordering = ['username']
    filter_horizontal = (
        "groups",
        "user_permissions",)
    
admin.site.register(User, UserAdmin)

