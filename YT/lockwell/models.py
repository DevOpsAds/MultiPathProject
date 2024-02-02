from django.contrib.auth.models import User
from django.db import models

from expense.models import CustomizingSpend
from app.models import (
    Active,
    Address,
    Document,
    TimeStampedModel,
    UuidModel,
    Financial,
    CreatedBy,
    RegisterCalendar,
    GrupAcessFor,
    Regions

)


# Lockwell_land repace: status testing models .ok
#CustomizingSpend
class mtb_Matrix (GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel): #classificaçao das rotinas

    evento_permitido = models.ForeignKey(
        CustomizingSpend,
        on_delete=models.CASCADE,
        verbose_name='Movimento configurado',
        related_name='expense',
    )

    matx_name = models.CharField('nome', max_length=255)

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('matx_name','evento_permitido')
        verbose_name = 'matrix'
        verbose_name_plural = 'matrices'

    def __str__(self):
        return str(self.matx_name)


#permite a integração em conformidade com o modelo ctb_agro windows: ok



#incorporando sublist em choque resolver problema Nome da tabela    lockwell_208_land_sub_list_name

class created_items (models.Model): #classificaçao das rotinas

    sub_matrix_id = models.ForeignKey(
        mtb_Sublist_matri,
        on_delete=models.CASCADE,
        verbose_name='create sub matrices',
        related_name='not_relate',
    )

    item_name = models.CharField('nome', max_length=100)
    
    type_item = models.CharField('tipo', max_length=100)

    STATUS = (
        ('texting', 'Texting'),
        ('creating', 'Creating'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    progress = models.CharField(
        max_length=8,
        choices=STATUS,
    )

  



    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('sub_matrix_id',)
        verbose_name = 'create_at_itens'
        verbose_name_plural = 'create_my_itens'



    @property
    def itens_list_create(self):
        return f' {self.sub_matrix_id or ""} {str("/->")} {self.item_name}'.strip()



    def __str__(self):
        return str(self.itens_list_create)

class relacionaSuppliers(models.Model): #classificaçao das rotinas




    category = models.ForeignKey(
        mtb_Matrix,
        on_delete=models.CASCADE,
        verbose_name='categoria',
        related_name='my_matrices',
        null=True,
        blank=True
    )



    sub_category = models.ForeignKey(
        mtb_Sublist_matri,
        on_delete=models.CASCADE,
        verbose_name='sub categoria',
        related_name='mtb_Sublist_matri',
        null=True,
        blank=True
    )



    prod_item = models.ForeignKey(
        created_items,
        on_delete=models.CASCADE,
        verbose_name='produto lista',
        related_name='created_items',
        null=True,
        blank=True
    )



    STATUS = (
        ('texting', 'Texting'),
        ('creating', 'Creating'),
        ('doing', 'Doing'),
        ('done', 'Done'),
    )

    progressRel = models.CharField(
        max_length=8,
        choices=STATUS,
        null=True,
        blank=True
    )



    createdrel_at = models.DateTimeField(auto_now_add=True,  null=True,
        blank=True)

    updatedrel_at = models.DateTimeField(auto_now=True,  null=True,
        blank=True)

    createdrel_by = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )



   #falta alguma coisa aqui
  

    @property
    def list_suppliers(self):
        return f' {self.suppliers or ""} {str("/->")} {self.category}'.strip()

    def __str__(self):
        return str(self.list_suppliers)










