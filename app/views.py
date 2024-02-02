from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User



# Create your views here.


# rota home pagina principal
def home(request):
    return render(request, 'home.html')


# formulário de cadastro
def create(request):
    return render(request, 'create.html')


# a inserção
def store(request):

    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senhas diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'],request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class']= 'alert-success'

    return render(request, 'create.html',data)

# rota painel entrada de dados de login
def painel(request):
    return render (request,'painel.html')


# rota dashboard
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] ='Usuário ou senha inválido'
        data['class'] = 'alert-danger'
        return render (request,'painel.html',data)



# pagina inicial dashboard

def dashboard(request):
    data = {}
    if  request.user.is_authenticated:
        return render (request,'dashboard/home.html')
    else:
        data['msg'] = 'Você não tem permissão de acesso!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

#rota de recuperção de password

def password(request):
    return render(request, 'password.html')

def dopassword(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senhas diferentes!'
        data['class'] = 'alert-danger'
        return render(request, 'password.html', data)
    else:
        user = User.objects.get(email_user="joaobatistalimajunior.ads@gmail.com")
        # user.set_password(request.POST['password'])
        # user.save()
        # data['msg'] = 'Nova senha cadastrada com sucesso!'
        # data['class'] = 'alert-success'
        # return redirect('/painel/',data)


def logout_view(request):
    logout(request)
    return redirect ('app:dashboard',)

