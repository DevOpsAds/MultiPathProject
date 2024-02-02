from django.contrib.auth.models import User
from django.db import models

from app.models import Regions
from app.models import Default_Address



# Create your models here.
class tb_fornecedor(Default_Address):  # classificaçao das rotinas
    trade_name = models.CharField('nome fantasia ', max_length=200)
    social_name = models.CharField('nome social ', max_length=200)


    email = models.EmailField('email', max_length=100,null=True, blank=True)
    cnpj = models.CharField('cnpj', max_length=18,null=True, blank=True)





    STATUS = (
        ('ET', 'Em teste'),
        ('Al', 'Analizase...'),
        ('Pd', 'Pendente.'),
        ('AP', 'Aprovado.'),
    )

    progress = models.CharField(
        max_length=8,
        choices=STATUS,
        null=True, blank=True
    )



    exist_deleted = models.BooleanField(
        'em uso /inativo',
        default=False,
        help_text='Se for True o item ativo em uso . Se for False o item está inativo.'

    )


    created_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    updated_at = models.DateTimeField(auto_now=True,null=True, blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name='usuário',
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('trade_name',)
        verbose_name = 'fornecedor'
        verbose_name_plural = 'fornecedores'



    def __str__(self):
        return str(self.trade_name)


    

        

#implementa ref. tbO_relcion_produto_agro_FORC_section_0
