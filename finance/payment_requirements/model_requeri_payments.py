from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


'''esta a parte sensivel do pagamenos '''



class PaymentRequirements (models.Model): #tratar a peculharidade e burocracia de cada pagameto pagamentos de um modo geral

    movement_date = models.DateField(
        'data', null=True, blank=True, default=now,
    )


class CreatedBy(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name='criado por',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True

class BankModel(models.Model):

    exist_bank = models.BooleanField(
        'Bancário -approved/rejected',
        default=False,
        help_text='Conceber privilégios: ° Atividadea esta conta. '

    )

    beneficiary_name = models.CharField('favorecido', max_length=50, help_text='nome do favorecido')

    branch = models.CharField('agencia', max_length=11, null=True, blank=True)

    account = models.CharField('conta', max_length=11, null=True, blank=True)

    operation = models.CharField('operção', max_length=7, null=True, blank=True)


    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'exist_bank:':self.exist_bank,
            'beneficiary_name': self.beneficiary_name,
            'branch': self.branch,
            'bank': self.bank,
            'account': self.account,
            'opration': self.opration,

        }




class PixModel(models.Model):

    exist_Pix = models.BooleanField(
        'PIX -approved/rejected',
        default=False,
        help_text='Conceber privilégios: ° Atividade PIX a esta conta.'

    )

    beneficiary_name = models.CharField('favorecido', max_length=50, help_text='nome do favorecido')

    phone = models.CharField(
        'n° telefone',
        max_length=11,
        unique=True,
        null=True,
        blank=True

    )

    mail = models.EmailField('E-mail',null=True, blank=True)

    randomKey = models.CharField('Chave aleatória', max_length=150, null=True, blank=True)



    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'beneficiary_name':self.beneficiary_name,
            'mail': self.mail,
            'randomKey':self.randomKey,
            'phone':self.randomKey,

        }


class moneyModel(models.Model):
    exist_dinheiro = models.BooleanField(
        'Dinheiro -approved/rejected',
        default=False,
        help_text='Conceber privilégios: ° Atividade em dinheiro a esta conta.'

    )

    paymentdate = models.DateField(
        'data', null=True, blank=True, default=now,
    )

    class Meta:
        abstract = True

    def to_dict_base(self):
        return {
            'exist_dinheiro': self.exist_dinheiro

        }


