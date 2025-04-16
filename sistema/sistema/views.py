from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        # Obter o nome de usuário e senha do formulário
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Tentar autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Se a autenticação for bem-sucedida, faça o login e redirecione
            login(request, user)
            return redirect('home')  # Substitua 'home' pela URL para onde o usuário será redirecionado após o login

        else:
            # Se o login falhar, mostre uma mensagem de erro
            messages.error(request, "Usuário ou senha inválidos.")
            return render(request, "login.html")
    
    return render(request, "login.html")
