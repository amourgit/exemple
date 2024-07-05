from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.

# Lister les articles
def List_Article(request):
    list_article = StockArticle.objects.all().filter(is_deleted=False)
    context = {
            'listes': list_article,
        }
    return render(request, 'profil.html', context)



# Modification d'un article
def Modif_Article(request, id):
    Article = StockArticle.objects.get(id=id)
    Article = ArticleForm(request.POST or None, instance=Article)
    if Article.is_valid():
        Article.save()
        message = "Successfull !"
    else:
        message = "Nous rencontrons une erreur !"
    context = {
            'Article': Article,
            'message': message
        }
    return render(request, 'profil.html', context)


# Ajout d'un article
def Ajout_Article(request):
    Article = ArticleForm(request.POST or None)
    if Article.is_valid():
        Article.save()
        message = "Successfull !"
    else:
        message = "Nous rencontrons une erreur !"
    Article = ArticleForm()
    context = {
            'utilisateur': Article,
            'message': message
        }
    return render(request, 'profil.html', context)


# Suppression d'un article
def Supp_Article(request, id):
    Article = StockArticle.objects.get(id=id)
    Article.is_deleted = True
    Article.save()
    message = "Successfull !"
    context = {
            'utilisateur': utilisateur,
        }
    return redirect('/')

