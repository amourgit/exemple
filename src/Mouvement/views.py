from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.

# Historique de Mouvement
def Historique_Mouvement(request):
    list_mouv = Mouvement.objects.all().filter(visible=True)
    user = request.user
    message = "Successfull !"
    context = {
            'list_mouv': list_mouv,
            'message': message,
            'user': user
        }
    return render(request, 'profil.html', context)



# Ajouter un Mouvement
def Ajout_Mouvement(request):
    Mouv = MouvementForm(request.POST or None)
    if Mouv.is_valid():
        Mouv.save()
        message = "Successfull !"
    else:
        message = "Nous rencontrons une erreur !"
        return render(request, {'message': message})
    Mouv = MouvementForm()
    context = {
            'Mouv': Mouv,
            'message': message
        }
    return render(request, 'profil.html', context)




# Modification d'un Mouvement
def Modif_Mouvement(request, id):
    try:
        type_mouvement = request.POST['type_mouvement']
        id_article = request.POST['libelle']
        quantite = request.POST['quantite']
        id_user = request.user.username
        motif = request.POST['motif']

        model = Mouvement.objects.get(id=id)
        model.type_mouvement = type_mouvement
        model.id_article = id_article
        model.quantite = quantite
        model.id_user = id_user
        model.motif = motif
        model.save()
        message = ""
    except:
        pass
    return redirect('/')


# Suppression d'un Mouvement
def Supp_Mouvement(request, id):
    Mouv = Mouvement.objects.get(id=id)
    Mouv.visible = False
    Mouv.save()
    message = "Successfull !"
    return redirect('/')