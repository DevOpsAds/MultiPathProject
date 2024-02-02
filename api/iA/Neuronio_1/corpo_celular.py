import pickle
from django.db.models import Q
from supplier.models import Supplier
from .nucleo_celular import nucleo_celular_start,Activation_nucleo_neural


def corpo_celular_start():

 
    print('**Corpo_celular_start ---------> Receptor PY em controle de caminho <-Aguardo acesso ao nucleo')
    print(nucleo_celular_start())
    progress = 'iA rede Neural !@@ -1 para controle ok confirmo corpo_celular ok atividade !:  controlle.py(copy@)'
    return progress

class Obturador_de_filds():
    print('RESPONSE CALL...')
   

    def obt_fields_empty (queryset):
        print('line:18**Corpo_celular ---------> confirma acesso a refinamento de obt_fields_empty para -> corpo_celular em listing')
        #campos=queryset.filter(email__isnull=True)
        #campos=Supplier.objects.all()
        #campos=queryset.filter()
        #campos=Supplier.objects.get(pk=12)
        #return(campos.email)
        #for e in queryset.filter():
        #    print (e.email)
        #    emails=e.nome
        #queuu=list(queryset.filter())
        #return(queuu[1])


        qs=Supplier.objects.filter(trade_name__isnull=False)
        for e in qs.filter():
            print (e.trade_name)
            emails=e.trade_name
            #(entrada,desejado,obtito,weight):
        neuronio_1=[1,0,1,0.2]
        dataset=[[0,0,0],
                 [0,1,0],
                 [1,0,0],
                 [1,1,1]]   
        print(Activation_nucleo_neural.perceptron_bitrain(dataset))

       
        return emails


                   



   
  
