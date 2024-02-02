from django.shortcuts import render,redirect

# Create your views here.
def printing(request):
    template_name = '/dashboard/'
    print('ativido o ----------------------modulo')
    return redirect(template_name)


