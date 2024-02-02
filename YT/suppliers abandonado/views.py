from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt

from .forms import SuppliersAll,StateForm,Suppliers_flash,Suppliers_sit_on_cad_use_updade
from .models import tb_fornecedor
from .filters import Pendencia_in_model,BossFilter2,BossFilter1

from address.models import Cep
from app.models import Regions,Default_Address


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


class SuppliersListView(View):

    def get(self,request):
        template_name = 'suppliers/suppliers_as_p.html'
        filter=BairrosFilter(request.GET, queryset=tb_fornecedor.objects.filt())
        return render(request,template_name,{'filter':filter})


class SuppliersCreateView(View):

    def get(self,request):
        template_name ='suppliers/suppliers_as_p.html'
        form = SuppliersAll(request.POST or None)
        context={'form':form}

        return render(request,template_name,context)        


def suppliers_list(request):
   

    #p_endereco=(Q(cep__isnull=True) | Q(endereco__isnull=True) | Q(address_number__isnull=True) |
     #Q(phone__isnull=True) | Q(complement__isnull=True) | Q(bairro__isnull=True) | Q(cidade__isnull=True) | Q(uf__isnull=True) |Q(trade_name__isnull=True)| Q(social_name__isnull=True) | Q(cnpj__isnull=True)| Q(progress__isnull=True)| Q(exist_deleted__isnull=True))
    
    object_list = tb_fornecedor.objects.all()
    form=Suppliers_flash#ajax
    template_name = 'suppliers/suppliers_list.html'
    print('line:70,def:filter_advancer,form page:views,evento_investigado:filter')
    context = {}

    context = {'object_list':object_list,'form':form}
    #field the search pesquisa?
    if request.method == 'GET':
    
     search= request.GET.get('btn_search')
     print('line:53,def: request,form page: views,evento_investigado: request search'+ str(search))

     if search is not None: 
        #pesquisa pendencia em endereços
        if search == 'pendencia':
            filter=Pendencia_in_model.f_pendencia(tb_fornecedor,tb_fornecedor)
            print('line:82,def:filter,form page:views ,_investigado:event bairros vazios ='+ str(filter))
            context = {'object_list':filter,'form':form}
           
            return render(request, template_name, context)


        elif search == 'pendet_list_endereco':
            filter=Pendencia_in_model.f_pendencia(Default_Address,tb_fornecedor)
            print('line:82,def:filter,form page:views ,_investigado:event bairros vazios ='+ str(filter))
            context = {'object_list':filter,'form':form}
           
            return render(request, template_name, context)

        #pesquisa pendencia em socil cadastro
        elif search == 'pendet_list_social':
            m_fields=['email','trade_name']
            filter=Pendencia_in_model.f_pendencia_fields_f(tb_fornecedor,tb_fornecedor,m_fields)            
            context = {'object_list':filter,'form':form}           
            return render(request, template_name, context)

        #pesquisa pendencia em situção cadastra,f_pendencia_fields_f
        elif search == 'pendet_list_sit_cad':
            m_fields=['progress','exist_deleted','trade_name']
            filter=Pendencia_in_model.f_pendencia_fields_f(tb_fornecedor,tb_fornecedor,m_fields)          
            context = {'object_list':filter,'form':form}           
            return render(request, template_name, context)


        elif search == 'location_region':
            #m_fields=['regions','trade_name']
            filter=Pendencia_in_model.f_pendencia_fields_f(tb_fornecedor,tb_fornecedor,m_fields)           
            context = {'object_list':filter,'form':form}           
            return render(request, template_name, context)         

        elif search == 'location_region_pk':
            loc_regions=request.GET.get('id_region')
            #object_list = tb_fornecedor.objects.filter(Q(regions__id__exact=loc_regions))
            context = {'object_list': object_list,'form':form}
            return render(request, template_name, context)


        elif search == 'location_district':            
            object_list = tb_fornecedor.objects.filter(Q(bairro__isnull=False))
            context = {'object_list': object_list,'form':form}
            return render(request, template_name, context)

        elif search == 'location_district_pk':
            l_districts=request.GET.get('id_bairro')
            #region=get_object_or_404(Regions,id=loc_regions)
            l_por_bairros = tb_fornecedor.objects.filter(Q(bairro=l_districts))
            print('line:147,def: id_bairros ,form page: views,evento_investigado: click location'+ str(l_por_bairros))
            context = {'object_list': l_por_bairros,'form':form}
            #context['object_list'] = l_regions
            return render(request, template_name, context)

     return render(request, template_name, context)

    elif request.method == 'POST':

     object_list = tb_fornecedor.objects.all()
     print(object_list)
     print('line:35,def: function,suppliers_list page: views,evento_investigado: submit filtrar'+ str(object_list))
     form=Suppliers_flash#ajax
     context = {'object_list': object_list,'form':form}
     return render(request, template_name, context)

def suppliers_create():
    ...

def suppliers_detail():
    ...

def suppliers_update():
    ... 

def suppliers_delete():
    ...   



class ListaBairrosView(View):

    def get(self,request):
        template_name = 'suppliers/suppliers_as_p.html'
        filter=BairrosFilter(request.GET, queryset=tb_fornecedor.objects.filt())

        return render(request,template_name,{'filter':filter})


class ListaBairrosView2(View):
    print('line:164,def: listar bairros com filter class cobination,form page:  and .filter ,evento_investigado: ListaBairrosView2'+ str(View))

    def get(self,request):
        template_name = 'suppliers/suppliers_as_p.html'
        filter=Pendencia_in_model.f_pendencia(Default_Address,tb_fornecedor)
        #filter=Pendencia_in_model(request.GET, queryset=tb_fornecedor.objects.all())

        print('line:174,def: quet filtera, form page: views,evento_investigado: filter de Pendencia_in_model:'+ str({filter}))
        return render(request,template_name,{'filtera':filter})



       
def suppliers_detaill(request, pk):
    template_name = 'suppliers/suppliers_detail.html'
    form=Suppliers_flash#ajax

    context = {}
   # regions =  request.GET.get('regions')
    

    obj = tb_fornecedor.objects.get(pk=pk)
    context = {'object': obj,'form':form}
   # context['form']=Suppliers_complet_endereco_cad_use_updade(regions)
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
       # regions=consulta.regions

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
     legenda_endereco=['Cep:','Endereco:','n°:','Tel:','Complemento:','Bairro:','Cidade:','Uf:','Região'] 
    # endereco=[cep,endereco,address_number,phone,complement,bairro,cidade,uf,regions]  
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
    print('Acesso ao save line: 259')
    data = {}

 
    
    user=User.objects.get(username='miguel')
    template_name = 'suppliers/suppliers_list.html'
    trade_name=request.POST.get('trade_name')
    cnpj=request.POST.get('cnpj')
    social_name=request.POST.get('social_name')
    email=request.POST.get('email')

    objects = tb_fornecedor(cnpj=cnpj,trade_name=trade_name,social_name=social_name,email=email,progress='1',created_by=user)
    form = Suppliers_flash
    print( "line 270  suppliers_as_p")
  
    if request.method == 'POST':
      
  
        print('is_valid form try save  item line:275- '+ request.POST.get('trade_name'))
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


    if request.method == 'GET':
        print('line:309,def: Get acesso in save ,form page: views,evento_investigado: form_filtros filter_advancer'+ str(request))
   
       

    return render(request, template_name,data)

@csrf_exempt
def suppliers_update_p(request):
    print('remova o csrf scrip de securt!!!!!!!!!!!!!@@@@@@@@@@@@@@@@@')
    
    

    template_name = 'suppliers/suppliers/41/'
    pk=request.POST.get('pk')
    objeto=get_object_or_404(tb_fornecedor,pk=pk)



    sit_cat=request.POST.get('sit_cat')
  
    endereco=request.POST.get('endereco')
    cad_social=request.POST.get('cad_social')
    template_name = 'suppliers/suppliers_detail.html'

    if (endereco):
      
     if (id_regions!=''):
        region=get_object_or_404(Regions,id=id_regions)

     else:
        region=get_object_or_404(Regions,id=4)

     print('acesso ao enderco atualizar concedido')
     print('pk user id'+objeto.trade_name)  
     template_name = 'suppliers/suppliers_detail.html'
     objeto.cep=request.POST.get('id_cep')
     objeto.endereco=request.POST.get('id_endereco')
     objeto.bairro=request.POST.get('id_bairro')
     objeto.cidade=request.POST.get('id_cidade')
     objeto.uf=request.POST.get('id_uf')
     objeto.address_number=request.POST.get('id_address_number')

     #objeto.regions=region
     
     print('meu objeto completo')
     
     #objeto.regions='pampulha'
    
     print('line 242. verificado post'+ str(objeto.address_number))
    
     objeto.phone=request.POST.get('id_phone')
     objeto.complement=request.POST.get('id_complemento')
     msg='Endereco ---- Alterado com sucesso!!'
     classAlert="alert alert-success"
    
    if(sit_cat):
     print('line :249 situacao_cad update suppliers') 
     print('acesso ao SIT_CAT atualizar concedido'+ request.POST.get('id_exist_deleted'))
     msg='Situação cadastrao  ---- Alterada atualizada  !'
     classAlert="alert alert-success"

     objeto.progress=request.POST.get('id_progress')
     if (request.POST.get('id_exist_deleted')=='true'):
      objeto.exist_deleted='True'
     else:
      objeto.exist_deleted='False'

     
    #form = Suppliers_flash(request.POST or None, instance=instance)
    print( "l235 suppliers_ update")
  
    if request.method == 'POST':


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
    template_name = 'suppliers/suppliers_as_p.html'
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
    region=get_object_or_404(Regions,id=1)
    objects = tb_fornecedor(cnpj=cnpj,trade_name='2222',social_name='24',progress='1',created_by=user)
    form = Suppliers_flash(request.POST or None)
   
   

    print( "line 365 suppliers_as_p")
  
    if request.method == 'POST':
        print( "line 368 formulario is_valid suppliers_as_p")
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
    template_name = 'suppliers/suppliers_as_p.html'
    
    country='Brasil'

    form = SuppliersAll('__all__')

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
            form = SuppliersAll(request.POST or None)
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
       
 

           
      

    
     
     context['form']=SuppliersAll(initial={
        
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
     template_name = 'suppliers/suppliers_as_p.html'
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

    
     
     context['form']=SuppliersAll(initial={
        'cep':cep,
        'bairro':bairro,
        'cidade':cidade,
        'endereco':endereco,
        'uf':uf,
        'country':country})
     return render(request,template_name,context)



class SuppliersSitCadModelCreate(CreateView):
    model=tb_fornecedor
    form_class=Suppliers_sit_on_cad_use_updade
    template_name= 'suppliers/modal_sit_cat.html'     

def SuppliersAll_sit_cad(request):
    template_name = 'suppliers/modal_sit_cat.html'
    form = Suppliers_sit_on_cad_use_updade(request.POST or None)
   

    if request.method == 'POST':
        if form.is_valid():
            #form.save()
            return redirect('suppliers/suppliers/41/information/')

    context = {'form': form}
    return render(request, template_name, context)