from django.contrib import admin
from django.contrib.admin import AdminSite

from address.models import city,distr,Cep,VinCep


from app.models import CallExpenseEleutero1vagao,CallMyMother,grandeza,Qualificar,Regions,base_name,base_name_Create,name_base_Convert
from api.models import CallApiQualificationGrandezas,CallApiQualification_grandezas_Person
from .models import Unit,Person, Photo, Routine,MovimentoConfig,Payment_methods
from expense.models import Spending,CustomizingSpend

from eleutero.models import Gn_noite,Gn_luz,Gn_ceu_terra,Gn,Fl1,Step_1,Step_2
from fl2.models import Fl2_Fl1,Fl2_Step_1,Fl2_Step_2



from marketing.models import MarketingCreate,MarketingAddSuppliers
from supplier.models import Var_meteorologicas,meterorologia,Supplier
from finance.models import Imposto,Ca,PaymentMethod,PrivilegesAccount,BalanceInitilAccount


from relacionChip.models import Cliente,Telefone,Mineralandia,Mineralandiafornecedor,Persona,District,City


class CadastroInlinebase_name(admin.TabularInline):
    model = base_name_Create
    extra = 0
class CadastroInline_Qualificar(admin.TabularInline):
    model = Qualificar
    extra = 1

class CadastroInline_Unit(admin.TabularInline):
    model = Unit
    extra = 0
class CadastroInline_Regions(admin.TabularInline):
    model = Regions
    extra = 1
class CadastroInline_Photo(admin.TabularInline):
    model = Photo
    extra = 3

class CadastroInline_Spending(admin.TabularInline):
    model = Spending
    extra = 0

class CadastroInline_Step_1(admin.TabularInline):
    model = Step_1
    extra = 0
    
class CadastroInline_person(admin.TabularInline):
    model = Person
    extra = 0

class CadastroInline_CallApiQualificationGrandezas(admin.TabularInline):
    model = CallApiQualificationGrandezas
    extra = 0


#ADRESS
@admin.register(city)
class AdressCityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uf')
    search_fields = ('name', )
    list_filter = ('uf',)

@admin.register(distr)
class distrAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)

@admin.register(Cep)
class CepAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'endereco')
    search_fields = ('cep','endereco')
    list_filter = ('endereco',)


@admin.register(VinCep)
class VinCepAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'endereco')
    search_fields = ('cep','endereco')
    list_filter = ('endereco',)






#APP
@admin.register(CallExpenseEleutero1vagao)
class CallExpenseEleutero_Admin(admin.ModelAdmin):
    inlines=(CadastroInline_Spending,CadastroInline_Step_1,)
    list_display = ('fk_matrix','call' ,'matrix_evolution',)
    list_display_links=('fk_matrix','matrix_evolution',)
    search_fields = ('matrix_evolution',)
    list_filter = ('matrix_evolution',)


@admin.register(CallMyMother)
class Matrix_Admin(admin.ModelAdmin):
    inlines=(CadastroInline_Unit,CadastroInline_Qualificar,CadastroInline_Regions,CadastroInline_Photo,)
    list_display = ('fk_matrix','call' ,'matrix_evolution',)
    list_display_links=('fk_matrix','matrix_evolution',)
    search_fields = ('matrix_evolution',)
    list_filter = ('matrix_evolution',)


@admin.register(grandeza)
class grandezaAdmin(admin.ModelAdmin):
    #inlines=(CadastroInline_Qualificar,)
    list_display = ('index', 'description',)
    list_display_links=('index',)
    search_fields = ('unidade',)
    list_filter = ('unidade',)


admin.site.register(base_name)


@admin.register(base_name_Create)


class base_name_CreateAdmin(admin.ModelAdmin):
    #inlines=(CadastroInlinebase_nameConvert,)
    list_display_links=('abreviacao',)
    list_display = ('index','abreviacao', 'description','fase_principal',)
    search_fields = ('abreviacao', 'name',)
    list_filter = ('abreviacao','name',)



admin.site.register(name_base_Convert)

admin.site.register(Regions)

#API
admin.site.register(CallApiQualificationGrandezas)

@admin.register(CallApiQualification_grandezas_Person)
class CallApiQualification_grandezas_Person_Admin(admin.ModelAdmin):
    inlines=(CadastroInline_CallApiQualificationGrandezas,)
    list_display = ('fk_matrix','fk_Person','call' ,'matrix_evolution',)
    list_display_links=('fk_matrix','matrix_evolution',)
    search_fields = ('matrix_evolution',)
    list_filter = ('matrix_evolution','fk_Person')

#CRM
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'active','cargo')
    # readonly_fields = ('slug',)
    # list_display_links = ('name',)
    search_fields = ('first_name', 'last_name', 'email','cargo')
    list_filter = ('active','cargo')
    # date_hierarchy = 'created'
    ordering = ('cargo',)
    # actions = ('',)

admin.site.register(Photo)

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'active','exist_deleted','progress','description','grup','created_by' )
    search_fields = ('modulo', 'first_name')
    list_filter = ('modulo',)

@admin.register(MovimentoConfig)
class MovimentoConfigAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', )
    search_fields = ('routine', 'name_conf')
    list_filter = ('grup','name_conf')

admin.site.register(Payment_methods)


#EXPENSE
@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'movement_expense', )
    search_fields = ('name', 'movement_expense',)
    list_filter = ('movement_expense',)

@admin.register(CustomizingSpend)
class CustomizingSpendAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_by','grup','spending_classify',)
    search_fields = ('name', 'spending_classify','spending_classify',)
    list_filter = ('created_by','grup','spending_classify',)


#ELEUTERO
class CadastroInlineStep_1(admin.TabularInline):
    model = Step_1
    extra = 0

class CadastroInlineStep_2(admin.TabularInline):
    model= Step_2
    extra=1

class CadastroInline_Gn_ceu_terra(admin.TabularInline):
    model = Gn_ceu_terra
    extra = 0

class CadastroInline_Gn_luz(admin.TabularInline):
    model = Gn_luz
    extra = 0

class CadastroInline_Gn_noite(admin.TabularInline):
    model = Gn_noite
    extra = 0

    

    


@admin.register(Fl1)
class Fl1Admin(admin.ModelAdmin):
    inlines=(CadastroInlineStep_1,CadastroInlineStep_2,)
    list_display = ('matx_name', 'active','exist_deleted', 'evento_permitido','grup',)
    list_display_links=('matx_name','grup',)
    search_fields = ('matx_name', 'evento_permitido',)
    list_filter = ('evento_permitido','grup',)

class CadastroInline_grandeza(admin.TabularInline):
    model = Step_1
    extra = 0
 
class CadastroInlineStep_2(admin.TabularInline):
    model= Step_2
    extra=1


@admin.register(Gn)
class GAdmin(admin.ModelAdmin):
    inlines=(CadastroInline_Gn_ceu_terra,CadastroInline_Gn_luz,CadastroInline_Gn_noite,)
    list_display = ('txt_name', 'call','index','coluna','grup',)
    list_display_links=('txt_name','grup',)
    search_fields = ('txt_name',)
    list_filter = ('txt_referncial','grup',)



@admin.register(Gn_ceu_terra)
class GnCeuTerraAdmin(admin.ModelAdmin):
    inlines=(CadastroInline_Gn_luz,CadastroInline_Gn_noite,)
    ordering=('-active',)
    list_display = ('active','exist_deleted','txt_name', 'call','index','coluna','grup',)
    list_display_links=('txt_name','grup',)
    search_fields = ('txt_name',)
    list_filter = ('txt_referncial','grup',)


@admin.register(Gn_luz)
class GnLuzAdmin(admin.ModelAdmin):
    ordering=('-active',)
    inlines=(CadastroInline_Gn_noite,)
    list_display = ('txt_name','active','exist_deleted','movement_date','grup',)
    #list_display_links=('txt_name','active','exist_deleted','progress','grup',)
    search_fields = ('txt_name',)
    list_filter = ('txt_name','active','movement_date','exist_deleted','grup',)

@admin.register(Gn_noite)
class GnNoiteAdmin(admin.ModelAdmin):
    ordering=('-active','inicio_date','fim_date')
    #inlines=(CadastroInline_Gn_ceu_terra,CadastroInline_Gn_luz,)
    list_display = ('inicio_date','fim_date','txt_name','active','exist_deleted','grup',)
    #list_display_links=('txt_name','active','exist_deleted','progress','grup',)
    search_fields = ('inicio_date','fim_date','txt_name',)
    list_filter = ('inicio_date','fim_date','txt_name','active','exist_deleted','grup',)

admin.site.register(Step_1)
class Step_1Admin(admin.ModelAdmin):

    list_display = ('step_number','__str__', 'active','movement_date','exist_deleted', 'name_step_listar','grup','created_by')
    search_fields = ('step_number', 'name_step_listar')
    list_display_links=('name_step_listar','grup')
    list_filter = ('step_number','evento_permitido','grup','created_by')

    admin.site.register(Step_2)
    




#FLII
class CadastroInlineFl2_Step_1(admin.TabularInline):
    model = Fl2_Step_1
    extra = 0

class CadastroInlineFl2_Step_2(admin.TabularInline):
    model= Fl2_Step_2
    extra=0

@admin.register(Fl2_Fl1)
class Fl2_Fl1Admin(admin.ModelAdmin):
    inlines=(CadastroInlineFl2_Step_1,)
    list_display = ('__str__', 'active','exist_deleted', 'fl2_evento_permitido','grup',)
    list_display_links=('fl2_evento_permitido',)
    search_fields = ('matx_name', 'fl2_evento_permitido',)
    list_filter = ('fl2_evento_permitido','grup',)



@admin.register(Fl2_Step_1)
class Fl2_Step_1Admin(admin.ModelAdmin):
    list_display = ('step_number','__str__', 'active','movement_date','exist_deleted', 'name_step_listar','grup','created_by')
    inlines=(CadastroInlineFl2_Step_2,)
    search_fields = ('step_number', 'name_step_listar')
    list_display_links=('name_step_listar',)
    list_filter = ('step_number','command_fl1','grup','created_by')
    
@admin.register(Fl2_Step_2)
class Fl2_Step_2Admin(admin.ModelAdmin):
    list_display = ('step_number','__str__', 'active','movement_date','created_by', 'item_name','grup',)
    search_fields = ('step_number', 'name_step_listar')
    list_filter = ('step_number','item_name','grup','created_by')
    




#MARKETING
admin.site.register(MarketingCreate)
admin.site.register(MarketingAddSuppliers)
#admin.site.register(LogMarket)

#SUPPLIER
class CadastroInline_var_meteriologica(admin.TabularInline):
    model = Var_meteorologicas
    extra = 0



@admin.register(meterorologia)
class meteorologiaAdmin(admin.ModelAdmin):
    inlines=(CadastroInline_var_meteriologica,)
    list_display = ('horadocsis','referencia', 'coletainfo3','coletainfo14','coletainfo9','coletainfo10','coletainfo12',)
    list_display_links=('coletainfo3',)
    search_fields = ('coletainfo14','coletainfo4',)
    list_filter = ('coletainfo14',)



@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = ('__str__', 'active','exist_deleted','cnpj')
    search_fields = ('cep','address','cnpj')
    list_filter = ('address','created_by','active')

#FINANCE
admin.site.register(Imposto)
admin.site.register(Ca)
admin.site.register(PaymentMethod)
admin.site.register(PrivilegesAccount)
admin.site.register(BalanceInitilAccount)

#RELATIONS CHIP
admin.site.register(Cliente)
admin.site.register(Telefone)
admin.site.register(Mineralandia)
admin.site.register(Mineralandiafornecedor)


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone',)
    search_fields = ('name', 'email')
    list_filter = ('gender',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'city')
    search_fields = ('name', 'city__name')
    list_filter = ('city',)



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uf')
    search_fields = ('name', )
    list_filter = ('uf',)



    





