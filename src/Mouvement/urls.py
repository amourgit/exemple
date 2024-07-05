from django.urls import path, include
from .views import *

app_name = 'Mouvement'

urlpatterns = [
    path('<int:id>/delete', Supp_Mouvement, name='mouv_sup'),
    #path('<int:id>/modif', Modif_Mouvement, name='mouv_modif'),
]