from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Article.models import StockArticle
from Article.forms import ArticleForm
from Mouvement.models import Mouvement
from Mouvement.forms import MouvementForm
from Utilisateur.forms import UserForm
from django.contrib.auth import get_user_model, authenticate, login, logout
User = get_user_model()
from .settings import BASE_DIR
from PIL import Image
# Ouvrir l'image JPEG

image_jpeg = Image.open(f'{BASE_DIR}/static/images/atec.jpg')

# Convertir en PNG
image_png = image_jpeg.convert('RGB')

# Enregistrer l'image PNG
image_png.save('atec.png', format='PNG')
print(image_png)


totaux = []


def Stock(lib):
    quantite_entre = 0
    quantite_sortie = 0
    l = Mouvement.objects.all().filter(id_article=lib, visible=True)
    for mouv in l:
        if mouv.type_mouvement == 'Entree':
            quantite_entre += mouv.quantite
        else:
            quantite_sortie += mouv.quantite
    elem = {
        'article': lib,
        'quantite_entre': quantite_entre,
        'quantite_sortie': quantite_sortie,
        'quantite_stock': quantite_entre - quantite_sortie,
    }
    return elem







def Dashboard(request):
    if not request.user.is_authenticated:
        return redirect('/connexion')
    list_libelles = []
    list_article = StockArticle.objects.all().filter(is_deleted=False)
    list_sortie =  Mouvement.objects.all().filter(visible=True, type_mouvement="Sortie")
    list_entree =  Mouvement.objects.all().filter(visible=True, type_mouvement="Entree")
    list_mouv =  Mouvement.objects.all().filter(visible=True)

    if request.method == 'POST':
        type_mouvement = request.POST['type_mouvement']
        id_article = request.POST['libelle']
        quantite = request.POST['quantite']
        id_user = request.user.username
        motif = request.POST['motif']
        id_article = StockArticle.objects.get(libelle=id_article)
        id_user = User.objects.get(username=id_user)
        Mouvement.objects.create(
            type_mouvement = type_mouvement,
            id_article = id_article,
            quantite = quantite,
            id_user = id_user,
            motif = motif,
        )
        return redirect('/')
    else:

        for article in list_article:
            totaux.append(Stock(article))
        
        for element in totaux:
            try:
                model = StockArticle.objects.get(libelle=element['article'])
                model.quantite = element['quantite_stock']
                model.save()
            except:
                pass
        
        list_article = StockArticle.objects.all().filter(is_deleted=False)
        list_sortie =  Mouvement.objects.all().filter(visible=True, type_mouvement="Sortie")
        list_entree =  Mouvement.objects.all().filter(visible=True, type_mouvement="Entree")
        list_mouv =  Mouvement.objects.all().filter(visible=True)
        user = f"Bienvenue Mr/Mme {request.user.username}."
        context = {
                'list_article': list_article,
                'list_sortie': list_sortie,
                'list_entree': list_entree,
                'list_mouv': list_mouv,
                'user': user,
                'lien_mere': BASE_DIR,
            }
        return render(request, 'dashboard.html', context)





def Connexion(request):
    if request.user.is_authenticated:
        message = 'Authentifié avec succes!'
        user = f"Bienvenue Mr/Mme {request.user.username}."
        context = {'user': user, 'message': message}
        return redirect('/')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            message = "Erreur d'authentification!"
            context = {'message': message}
            return render(request, 'connexion.html', context)
    return render(request, 'connexion.html')

def Deconnexion(request):
    logout(request)
    return redirect('/connexion')