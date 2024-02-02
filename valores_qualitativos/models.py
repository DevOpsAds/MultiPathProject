from django.contrib.auth.models import User
from django.db import models
from eleutero.models import Fl1
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
    RegisterCaledarTime,
    GrupAcessFor,
    Regions

)


# Lockwell_land repace: status testing models .ok
#CustomizingSpend
class val_Fl1 (GrupAcessFor,Active,CreatedBy,RegisterCalendar,TimeStampedModel): #classificaçao das rotinas

    evento_permitido = models.ForeignKey(
        Fl1,
        on_delete=models.CASCADE,
        verbose_name='matrix_eleutero',
        related_name='matriz_Eleutero',
    )

    matx_name = models.CharField('nome', max_length=255)

    description = models.TextField()



    pk_created_user = models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('matx_name','evento_permitido')
        verbose_name = 'val_matrix'
        verbose_name_plural = 'valores_matrices'

    def __str__(self):
        return str(self.matx_name)





