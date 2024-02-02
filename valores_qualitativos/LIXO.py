
class Step_1 (GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas
    
    step_number=models.IntegerField('passo', null=True, blank=True)

    command_fl1 = models.ForeignKey(
        Fl1,
        on_delete=models.CASCADE,
        verbose_name='autorizador',
        related_name='matrix',
    )

    name_step_listar = models.CharField('listar', max_length=100)

    STATUS = (
        ('1', 'Esperando'),
        ('2', 'Atrasado'),
        ('3', 'problema'),
        ('4', 'Preparando'),
    )

    progress = models.CharField(
        max_length=10,
        choices=STATUS,
    )

    description = models.TextField()



    created_user= models.ForeignKey(
        User,
        default=1,
        on_delete=models.SET_NULL,
        related_name='%(class)screate',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('step_number','command_fl1')
        verbose_name = 'matrix 1'
        verbose_name_plural = ' passo'

    @property
    def sub_list_matrix(self):
        return f' {self.command_fl1 or ""} {str("/->")} {self.name_step_listar}'.strip()

    def __str__(self):
        return str(self.sub_list_matrix)


class Step_2 (Fl1,GrupAcessFor,Active,CreatedBy,TimeStampedModel,RegisterCaledarTime): #classificaçao das rotinas

	step_number=models.IntegerField('passo', null=True, blank=True)
    


	step = models.ForeignKey(
		Step_1,
		on_delete=models.CASCADE,
		verbose_name='tarf',
		related_name='matrix',
    )

	item_name = models.CharField('nome', max_length=100)
    
	type_item = models.CharField('tipo', max_length=100)

	STATUS = (
		('1', 'Esperando'),
		('2', 'Atrasado'),
		('3', 'problema'),
		('4', 'Preparando'),
	)


	progress = models.CharField(
		max_length=10,
		choices=STATUS,
	)


	class Meta:
		ordering = ('step','step_number',)
		verbose_name = 'items'
		verbose_name_plural = 'create_my_itens'

	@property
	def itens_list_create(self):
		return f' {self.step or ""} {str("/->")} {self.item_name}'.strip()

	def __str__(self):
		return str(self.type_item)





