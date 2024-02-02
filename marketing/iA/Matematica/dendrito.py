from .corpo_celular import math_corpo_celular_start,math_Obturador_de_filds
import django_filters
from django.db.models import Q
from supplier.models import Supplier
#from address.models import Cep
#from app.models import Regions,Default_Address



def math_dentrito_start():

    print('math_:line:12,dendrito.py**Dendrito ---------> confirma controle para -> corpo_celular em listing')
    print(math_corpo_celular_start())
    progress = 'math_:line:14,iA rede Neural !@@ -1 para controle ok confirmo dedrito atividade !:  controlle.py(copy@)'
    return progress


class math_Table_studie():
        print('math_:line:19,dendrito.pyRESPONSE CALL...')
        print('math_:line:19,dendrito.py**Dendrito ---------> confirma acesso a Table_studie  para -> corpo_celular em listing')

        #functions de pendencial -verificar se a dados em isNULL em models
        def math_fields_empty (model_vinculado,model_investig):
            #Obter todos os campos do modelo a investigado.
            obten_fields= model_vinculado._meta.get_fields()
                   
            #crie uma lista de filtros Q a serem verificados 
            filtros_null=[Q(**{campo.name +'__isnull':True})
            for campo in obten_fields
                if campo.name != 'id'
            ]
            
            #uso do opredaor logio OR para combinar todos os campos
            filtro_completo=filtros_null.pop()
            for filtro in filtros_null:
                filtro_completo |= filtro
                #filtre os registro em NULL ja na tabela interessadas

            registros_null= model_investig.objects.filter(filtro_completo)
           
            


            if (registros_null):
                #print('line:42 .dentrito Obturador_de_filds:',Obturador_de_filds.obt_fields_empty(registros_null))   
                 print(math_Obturador_de_filds.math_obt_fields_empty(registros_null))           
        
            #print('line:39,def: campos detrito.py ,form page: .estudo_tabela ,evento_investigado: registros_null'+ str(registros_null))
            return registros_null.order_by('trade_name')
        
        class Meta:
            fields = ['f_pendencia']
            ordering = 'pk' 