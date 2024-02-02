

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
        verbose_name_plural = 'create sub matrices'

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




 migrations.CreateModel(
            name='Step_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now=True, verbose_name='criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('situacao', models.CharField(blank=True, choices=[('1', 'Aprovado'), ('2', 'Aguardando'), ('3', 'Avaliando'), ('4', 'Analise'), ('5', 'Paralizado'), ('6', 'Pendente'), ('7', 'Negado')], default=2, max_length=20, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='ativo')),
                ('exist_deleted', models.BooleanField(default=True, help_text='Se for True o item existe. Se for False o item foi deletado.', verbose_name='existe/deletado')),
                ('movement_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='data/hora')),
                ('step_number', models.IntegerField(blank=True, null=True, verbose_name='passo')),
                ('item_name', models.CharField(max_length=100, verbose_name='nome')),
                ('type_item', models.CharField(max_length=100, verbose_name='tipo')),
                ('progress', models.CharField(choices=[('1', 'Esperando'), ('2', 'Atrasado'), ('3', 'problema'), ('4', 'Preparando')], max_length=10)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='privilegio')),
                ('grup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.group', verbose_name='Acessível para grup')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matrix', to='eleutero.step_1', verbose_name='tarf')),
            ],
            options={
                'verbose_name': 'items',
                'verbose_name_plural': 'itens',
                'ordering': ('step', 'step_number'),
            },
        ),