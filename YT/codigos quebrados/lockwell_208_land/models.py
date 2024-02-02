from django.contrib.auth.models import User
from django.db import models

from app.models import Regions
from suppliers.models import tb_fornecedor


# Lockwell_land models .ok

class mtb_Matrix (models.Model): #classificaçao das rotinas

    matx_name = models.CharField('nome', max_length=255)

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
        ordering = ('pk',)
        verbose_name = 'matrix'
        verbose_name_plural = 'matrices'

    def __str__(self):
        return str(self.matx_name)


#permite a integração em conformidade com o modelo ctb_agro windows: ok
class mtb_Sublist_matri (models.Model): #classificaçao das rotinas

    catergory = models.ForeignKey(
        mtb_Matrix,
        on_delete=models.CASCADE,
        verbose_name='categoria',
        related_name='matrix',
    )

    sub_list_name = models.CharField('tipo', max_length=100)

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
        ordering = ('catergory','sub_list_name')
        verbose_name = 'sub_matrix'
        verbose_name_plural = 'my_matrices'

    @property
    def sub_list_matrix(self):
        return f' {self.catergory or ""} {str("/->")} {self.sub_list_name}'.strip()

    def __str__(self):
        return str(self.sub_list_matrix)

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
        ordering = ('item_name',)
        verbose_name = 'create_at_itens'
        verbose_name_plural = 'create_my_itens'



    @property
    def itens_list_create(self):
        return f' {self.sub_matrix_id or ""} {str("/->")} {self.item_name}'.strip()



    def __str__(self):
        return str(self.itens_list_create)

# implement relation chip entre supplier and intens
class tb_relacion_itens_suppliers (tb_fornecedor #classificaçao das rotinas



    suppliers = models.ForeignKey(
        tb_fornecedor,
        on_delete=models.CASCADE,
        verbose_name='fornecedor',
        related_name='tb_fornecedor',
    )

    category = models.ForeignKey(
        mtb_Matrix,
        on_delete=models.CASCADE,
        verbose_name='categoria',
        related_name='my_matrices',
    )



    sub_category = models.ForeignKey(
        mtb_Sublist_matri,
        on_delete=models.CASCADE,
        verbose_name='sub categoria',
        related_name='mtb_Sublist_matri',
    )



    prod_item = models.ForeignKey(
        created_items,
        on_delete=models.CASCADE,
        verbose_name='produto lista',
        related_name='created_items',
    )



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

    created_by = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )



    class Meta:
        ordering = ('suppliers')
        verbose_name = 'vincule_force'
        verbose_name_plural = 'tb_relacion_itens_suppliers'

    @property
    def list_suppliers(self):
        return f' {self.suppliers or ""} {str("/->")} {self.category}'.strip()

    def __str__(self):
        return str(self.list_suppliers)








