import django_filters
from django.db.models import Q
from .models import tb_fornecedor
from address.models import Cep
from app.models import Regions,Default_Address


class BairrosFilter (django_filters.FilterSet):
		

		class Meta:
			models= tb_fornecedor
			fields = ['regions']



class BossFilter2 (django_filters.FilterSet):
		#filtro para região
		#regiao =django_filters.CharFilter(field_name='regions',lookup_expr='exact')
		print('line:16,def: BossFilter2,form page: .filter_bairros_com_pi,evento_investigado: class info')
		#filtro para bairros começados por ""pi"
		bairros=django_filters.CharFilter(field_name='regions',lookup_expr='istartswith')
		print('line:16,def: BossFilter2,form page: .filter_bairros_com_pi,evento_investigado: class info'+str(bairros))
	   

		class Meta:
			model = tb_fornecedor
			fields = ['bairros']

		def filter_bairros_com_pi(self,queryset,name,value):
			print('line:line:25 ,def: function,form page: views,evento_investigado: event'+ str(debug))
			return queryset.filter(bairros_com_pi__iexact='22')



class BossFilter1 (django_filters.FilterSet):
		#filtro para região
		#regiao =django_filters.CharFilter(field_name='regions',lookup_expr='exact')
		print('line:35,def: BossFilter2,form page: .filter_bairros_com_pi,evento_investigado: class info')
		#filtro para bairros começados por ""pi"
		p_endereco = tb_fornecedor.objects.filter(regions='1' )
		print('line:36,def: BossFilter2,form page: .filter_bairros_com_pi,evento_investigado: class info'+str(p_endereco))
	   

		class Meta:
			
			fields = ['p_endereco']

		

class Passport():
		#class responde por  functions_fitros em chaves estrangeiros 


		#functions de pendencial -verificar se a dados em isNULL em models
	    def f_pendencia (fk,model_investig):
	    	#Obter todos os campos do modelo a investigado.
	    	loc_regions=request.GET.get(fk)
	    	obten_fields= model_vinculado._meta.get_fields()
	    	print('line:58,def: obten_fields,form page: views,evento_investigado: obten_fields'+ str(obten_fields))
	   
	    	#crie uma lista de filtros Q a serem verificados 
	    	filtros_null=[Q(**{campo.name +'__isnull':True})
	     	for campo in obten_fields if campo.name != 'id'
	    	]
	    	#uso do opredaor logio OR para combinar todos os campos
	    	filtro_completo=filtros_null.pop()
	    	for filtro in filtros_null:
	        	filtro_completo |= filtro
	    		#filtre os registro em NULL ja na tabela interessadas
	    	registros_null= model_investig.objects.filter(filtro_completo)
	    	return registros_null.order_by('trade_name')

	    

	    #functions de pendencial -verificar se a dados em isNULL por models em fields pratics
	    def f_pendencia_fields_f (model_vinculado,model_investig,myfield):
	    	#Obter todos os campos do modelo a investigado.
	    	obten_fields=myfield
	    	#crie uma lista de filtros Q a serem verificados 
	    	filtros_null=[Q(**{campo +'__isnull':True})for campo in obten_fields
	    	]
	    	#uso do opredaor logio OR para combinar todos os campos
	    	filtro_completo=filtros_null.pop()
	    	for filtro in filtros_null:
	        	filtro_completo |= filtro
	    		#filtre os registro em NULL ja na tabela interessadas
	   
    	
	    		#filtre os registro em NULL ja na tabela interessadas
	    	registros_null= model_investig.objects.filter(filtro_completo).values(*obten_fields)
	    	
	    
	    	print('line:89,def: campos dedicados,form page: .filter,evento_investigado: registros_null'+ str(registros_null))
	    	return registros_null.order_by('trade_name')
	    
	    class Meta:
		    fields = ['f_pendencia']
		    ordering = 'registros_null' 


class Pendencia_in_model ():


		#functions de pendencial -verificar se a dados em isNULL em models
	    def f_pendencia (model_vinculado,model_investig):
	    	#Obter todos os campos do modelo a investigado.
	    	obten_fields= model_vinculado._meta.get_fields()
	    	print('line:58,def: obten_fields,form page: views,evento_investigado: obten_fields'+ str(obten_fields))
	   
	    	#crie uma lista de filtros Q a serem verificados 
	    	filtros_null=[Q(**{campo.name +'__isnull':True})
	     	for campo in obten_fields if campo.name != 'id'
	    	]
	    	#uso do opredaor logio OR para combinar todos os campos
	    	filtro_completo=filtros_null.pop()
	    	for filtro in filtros_null:
	        	filtro_completo |= filtro
	    		#filtre os registro em NULL ja na tabela interessadas
	    	registros_null= model_investig.objects.filter(filtro_completo)
	    	return registros_null.order_by('trade_name')

	    

	    #functions de pendencial -verificar se a dados em isNULL por models em fields pratics
	    def f_pendencia_fields_f (model_vinculado,model_investig,myfield):
	    	#Obter todos os campos do modelo a investigado.
	    	obten_fields=myfield
	    	#crie uma lista de filtros Q a serem verificados 
	    	filtros_null=[Q(**{campo +'__isnull':True})for campo in obten_fields
	    	]
	    	#uso do opredaor logio OR para combinar todos os campos
	    	filtro_completo=filtros_null.pop()
	    	for filtro in filtros_null:
	        	filtro_completo |= filtro
	    		#filtre os registro em NULL ja na tabela interessadas
	   
    	
	    		#filtre os registro em NULL ja na tabela interessadas
	    	registros_null= model_investig.objects.filter(filtro_completo).values(*obten_fields)
	    	
	    
	    	print('line:89,def: campos dedicados,form page: .filter,evento_investigado: registros_null'+ str(registros_null))
	    	return registros_null.order_by('trade_name')
	    
	    class Meta:
		    fields = ['f_pendencia']
		    ordering = 'registros_null' 


