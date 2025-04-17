from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.views import View

def login_view(request):
    if request.method == "POST":
        # Obter o nome de usuário e senha do formulário
        usuario = request.POST["usuario"]
        senha = request.POST["senha"]
        
        # Tentar autenticar o usuário
        user = authenticate(request, username=usuario, password=senha)
        
        if user is not None:
            # Se a autenticação for bem-sucedida, faça o login e redirecione
            if user.is_active:
                login(request, user)
                return redirect('/veiculos')

        else:
            # Se o login falhar, mostre uma mensagem de erro
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, "autenticacao.html")
    
    return render(request, "autenticacao.html")

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)