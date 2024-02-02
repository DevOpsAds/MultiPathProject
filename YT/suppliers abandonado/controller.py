from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from .forms import SuppliersAll,StateForm,Suppliers_flash
from django.core.exceptions import ObjectDoesNotExist
from address.models import Cep
from .models import tb_fornecedor
from django.views.decorators.csrf import csrf_exempt

#from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime
#from .models import Mineralandia,Cliente,Telefone,City,District,Persona
from address.views import filter_cep,address_as_p

# Create your views here.
def printing(request):
 
    template_name = 'suppliers/myPost.html'
    print('ativido o ----------------------modulo')
    msg="reenviando por context"
    classAlert="alert alert-info"
    context = {'msg':msg ,'class':classAlert}
    return render(request, template_name, context)

def suppliers_list(request):
    template_name = 'suppliers/suppliers_list.html'
    object_list = tb_fornecedor.objects.all()
    print(object_list)
    form=Suppliers_flash#ajax
    context = {'object_list': object_list,'form':form}
    return render(request, template_name, context)


def suppliers_detaill(request, pk):
    template_name = 'suppliers/suppliers_detail.html'
    form=Suppliers_flash#ajax
    obj = tb_fornecedor.objects.get(pk=pk)
    context = {'object': obj,'form':form}
    return render(request, template_name, context)


#capturar informaçoes suppliers
def suppliers_det_informat(request, pk):
    template_name = 'suppliers/pendet_list.html'
    form=Suppliers_flash#ajax
    consulta = tb_fornecedor.objects.get(pk=pk)
   
    if request.method == 'GET':
        print('view suppliers_pendent_list- filter_cep flou 44')
        print(consulta.cep)
        cep=consulta.cep
        endereco=consulta.endereco
        address_number=consulta.address_number
        phone=consulta.phone
        complement=consulta.complement
        bairro=consulta.bairro
        cidade=consulta.cidade
        uf=consulta.uf

        trade_name=consulta.trade_name
        social_name=consulta.social_name
        email=consulta.email
        cnpj=consulta.cnpj

        progress=consulta.progress
        exist_deleted=consulta.exist_deleted
        created_at=consulta.created_at
        updated_at=consulta.updated_at
        created_by=consulta.created_by
   
    try:
 
     print('view suppliers_pendent_list- informat flou 52')

       
  

     
     #arrays com legendas  
     legenda_endereco=['Cep:','Endereco:','n°:','Tel:','Complemento:','Bairro:','Cidade:','Uf:'] 
     endereco=[cep,endereco,address_number,phone,complement,bairro,cidade,uf]  
     legenda_contato_social=['Nome fantazia:', 'Nome razão social', 'Email', 'CNPJ']
     contato_social=[trade_name, social_name, email, cnpj]
     legenda_situacao=['Qualidade do cadastro;','Atividade ou Inativo:','Criado em:','Ultima modifição:']
     situacao=[progress,exist_deleted,created_at,updated_at]
     #verifica pendencia em enderços
     temVazio = False
     for elmento in endereco:
        if not elmento:
         temVazio= True
         break

     if temVazio:
        comp_endereco='incompleto'
     else:
        comp_endereco=''  

     #verifica pendencia no cadastro social
     temVazio = False
     for elmento in contato_social:
        if not elmento:
         temVazio= True
         break

     if temVazio:
        comp_social='incompleto'
     else:
        comp_social=''

    #verifica pendencia no cadastro situação e contato
     temVazio = False
     for elmento in situacao:
        if not elmento:
         temVazio= True
         break

     if temVazio:
        comp_situacao='incompleto'
     else:
        comp_situacao=''

     legenda_data=['Endereço','Contato','R. social']
     data=[comp_endereco,comp_social,comp_situacao] 

     print('view suppliers_pendent_list- informat?  contex send..flou 120')
     context = {
        
        'data': zip(data,legenda_data),
        'endereco':zip(endereco,legenda_endereco),
        'contato_social':zip(contato_social,legenda_contato_social),
        'situacao':zip(situacao,legenda_situacao)
        }
     #verificar se a request veio por ajax
     if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
        print('request for ajax')
        return JsonResponse({
        'data': data,
        'endereco':endereco,
        'contato_social':contato_social,
        'situacao':situacao
        })

     return render(request, template_name, context)


    except ObjectDoesNotExist:
        bairro=''
        cidade=''
        endereco=''
        uf=''
        print('view suppliers_detail- filter_cep flou 69')
    comp_endereco="1"
    comp_situacao="0"
    comp_social="1"  


    data=[comp_endereco,comp_contato,comp_social]
    endereco=[cep,endereco,address_number,phone,complement,bairro,cidade,uf,]  
    contato_social=[trade_name, social_name, email, cnpj]
    situacao==[progress,exist_deleted,created_at,updated_at,created_by,]


    

    print('view suppliers_detail- filter_cep flou 73')
     
    return JsonResponse({
        'data': data,
        'endereco':endereco,
        'contato_social':contato_social,
        'situacao':situacao
        })


def suppliers_save_p(request):
    print('Acesso ao save')
    data = {}

 
    
    user=User.objects.get(username='miguel')
    template_name = 'suppliers/suppliers_list.html'
    trade_name=request.POST.get('trade_name')
    cnpj=request.POST.get('cnpj')
    social_name=request.POST.get('social_name')
    email=request.POST.get('email')

    objects = tb_fornecedor(cnpj=cnpj,trade_name=trade_name,social_name=social_name,email=email,progress='1',created_by=user)
    form = Suppliers_flash
    print( "l35 suppliers_as_p")
  
    if request.method == 'POST':
      
  
        print('is_valid form try save  item line:194- '+ request.POST.get('trade_name'))
        comp_endereco="1"
        comp_contato="0"
        comp_social="1"  


        data=[comp_endereco,comp_contato,comp_social,trade_name,email, data['msg'],data['class']]
        objects.save()
         #consulta = tb_fornecedor.objects.all()
        trade_name=trade_name
        #social_name=social_name
        email=email
        # cnpj=objects.cnpj


     
        return JsonResponse({
        'data': data,
        
        })

    else:   
            data['msg'] = 'Senha e confirmação de senhas diferentes!'
            data['class'] = 'alert-danger' 
                

    #context = {'form': form}
    print( "l57 data--"+ data['msg'] )
   
       

    return render(request, template_name,data)

@csrf_exempt
def suppliers_update_p(request):
    print('remova o csrf scrip de securt!!!!!!!!!!!!!@@@@@@@@@@@@@@@@@')
  
    template_name = 'suppliers/suppliers/41/'
    pk=request.POST.get('pk')
    objeto=get_object_or_404(tb_fornecedor,pk=pk)
    print('pk user id'+objeto.trade_name)  
    template_name = 'suppliers/suppliers_detail.html'
    objeto.cep=request.POST.get('id_cep')
    objeto.endereco=request.POST.get('id_endereco')
    objeto.bairro=request.POST.get('id_bairro')
    objeto.cidade=request.POST.get('id_cidade')
    objeto.uf=request.POST.get('id_uf')
    objeto.address_number=request.POST.get('id_address_number')
    print('line 242. verificado post'+ objeto.address_number)
    
    objeto.phone=request.POST.get('id_phone')
    objeto.complement=request.POST.get('id_complemento')
   
    #form = Suppliers_flash(request.POST or None, instance=instance)
    print( "l235 suppliers_ update")
  
    if request.method == 'POST':

        msg='Endereco ---- Alterado com sucesso!!'
        classAlert="alert alert-success"
        print('is_valid form try update  item line:243- '+request.POST.get('id_endereco'))
    


        data=[msg,classAlert]
        objeto.save()
        #consulta = tb_fornecedor.objects.all()
        print('line 254 confirme a informaçoes para atualizar o update em:'+ str(objeto.cep))
        
        
        #verificar se a request veio por ajax
        if request.META.get('HTTP_X_REQUESTED_WITH')=='XMLHttpRequest':
          print('request for ajax')
          return JsonResponse({
          'data': data
          })
        context = {'data': data,'form':form}
        return render(request, template_name, context)

    return render(request,"request.method")




def pd_redirect(request):
    template_name = 'suppliers/suppliers_form_as_p.html'
    form = SuppliersForm0(request.POST or None)
   

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crm/person_list/')

    context = {'form': form}
    return render(request, template_name, context)


def suppliers_as_p(request):
    print('creando formulario flash line:45 views')
    user=User.objects.get(username='miguel')
    template_name = 'suppliers/suppliers_as_p.html'
    cnpj='1234'
    objects = tb_fornecedor(cnpj=cnpj,trade_name='24',social_name='24',progress='1',created_by=user)
    form = Suppliers_flash(request.POST or None)
   
   

    print( "l42 suppliers_as_p")
  
    if request.method == 'POST':
        if form.is_valid():

            objects.save()
            return redirect('/crm/person_list/')

    context = {'form': form}
    return render(request, template_name, context)

def suppliers_as_p_mod(request):
    user=User.objects.get(username='miguel')
    template_name = 'suppliers/suppliers_list.html'
    cnpj='1234'
    objects = tb_fornecedor(cnpj=cnpj,trade_name='24',social_name='24',progress='1',created_by=user)
    form = SuppliersForm0(request.POST or None)
   
   

    print( "l42 suppliers_as_p")
  
    if request.method == 'POST':
        if form.is_valid():
            
            objects.save()
            return redirect('/suppliers/suppliers_list/')

    context = {'form': form}
    return render(request, template_name, context)

def suppliers_as_p_inativate(request):
    template_name = 'suppliers/suppliers_form_as_p.html'
    
    country='Brasil'

    form = Suppliers_Form('__all__')

    context = {'form': form}
   

    if request.method == 'POST':
     print(request.POST.get('cep'))
    
     country='Brasil'

     
     try: 

            cep=request.POST.get('cep')
            consulta=Cep.objects.get(cep=cep)
            trade_name=request.POST.get('trade_name')
            social_name=request.POST.get('social_name')
            bairro=consulta.bairro
            cidade=consulta.cidade
            endereco=consulta.endereco
            uf=consulta.uf
            print("chegou um--------------suple create------.l62------------------- post"+cep+bairro+social_name)
            form = Suppliers_Form(request.POST or None)
            if request.method == 'POST':
              if form.is_valid():
               print('@@@@@@is_valid l66')
               form.save()
               return redirect('/crm/person_list/')
           

    
 

        
  
         
              
     except ObjectDoesNotExist:

            bairro='não localizado'
            cidade='não localizado'
            endereco='não localizado'
            uf='x'
            print(cep)
   
       

     if request.method == 'GET':
      print("chegou um--------------suple create------------------------- get")
      cep= request.GET.get('cep')
        
     try:
        consulta=Cep.objects.get(cep=cep)
        print("entrou .l94 get")
        
        bairro=consulta.bairro
        cidade=consulta.cidade
        endereco=consulta.endereco
        uf=consulta.uf
        if form.is_valid():
           print('@@@@@@is_valid l101*')
           form.save()
           print('.l103*'+cep)
           return redirect('/crm/person_list/')
        
     except ObjectDoesNotExist:
        print('estado de  -----------direcionado para filter por (doesNot)')
        #return redirect('/suppliers/filter_cep/?cep='+cep)
        bairro='não existe'
        cidade='não existe'
        endereco='não localizado'
        uf='--'
        print(cep)
       
 

           
      

    
     
     context['form']=Suppliers_Form(initial={
        
        'cep':cep,
        'bairro':bairro,
        'cidade':cidade,
        'endereco':endereco,
        'uf':uf,
        'country':country})

  
  
    print('renderizou e devolveu por suppliers create-------------------------')
    return render(request,template_name,context)

#este funiciona parcial precisa de mais teste
def filter_cep_inativo(request):
     template_name = 'suppliers/suppliers_form_as_p.html'
     context = {}
     country='Brasil'
     
     try:
            cep=" "
            bairro="-?-"
            cidade="-?-"
            endereco="-?-"
            uf="-*"
            print(cep)
         
         
              
     except ObjectDoesNotExist:

            bairro='não localizado'
            cidade='não localizado'
            endereco='não localizado'
            uf='x'
            print(cep)
   
       

     if request.method == 'GET':
      
      print("chegou um get")
      
      cep = request.GET.get('cep')

      


        
     try:
        consulta=Cep.objects.get(cep=cep)
        print("entrou get")
        bairro=consulta.bairro
        cidade=consulta.cidade
        endereco=consulta.endereco
        uf=consulta.uf
        print(cep)
       


          
     except ObjectDoesNotExist:
        bairro='não existe'
        cidade='não existe'
        endereco='não localizado'
        uf='--'
        print(cep)
       
 

           
        print(cep)

    
     
     context['form']=Suppliers_Form(initial={
        'cep':cep,
        'bairro':bairro,
        'cidade':cidade,
        'endereco':endereco,
        'uf':uf,
        'country':country})
     return render(request,template_name,context)