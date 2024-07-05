from django.shortcuts import render
from .forms import *
from .models import *


def Modif_User(request):
    message = ''
    username = request.user.username
    user = User.objects.get(username=username)
    user = UserForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if user.is_valid():
            user.save()
            message = "Successfull !"
            return redirect('')
    context = {
            'user': user,
            'message': message
        }
    return render(request, 'profil.html', context)