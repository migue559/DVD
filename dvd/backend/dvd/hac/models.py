from django.contrib.auth.models import Group
from django.db.models import Q
from dvd.core.models import *
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder
import json

##############################################################
################ Catálogos HIVE ##############################
##############################################################
class HiveCatalogue(ModelBase):
    name = models.CharField(verbose_name='nombre',max_length=50, help_text='Nombre del catálogo')
    description = models.TextField(verbose_name='descripcion',help_text='Descripción del catálogo')
    catalogue = models.CharField(verbose_name='id',max_length=150, help_text='Id del catálogo')
    twoValidation = models.BooleanField(verbose_name='doble validacion',default=False, help_text='Bandera de si existe catálogo o si esta activo o no')
    administrators = models.ManyToManyField(User, related_name='+', verbose_name='Lider de Gobierno de datos')
    superUsers = models.ManyToManyField(User, blank=True, related_name='+', verbose_name='Editores')
    superGroups = models.ManyToManyField(Group, blank=True, related_name='+')
    users = models.ManyToManyField(User, blank=True, related_name='+', verbose_name='Visualizadores')
    groups = models.ManyToManyField(Group, blank=True, related_name='+')
    isPublic = models.BooleanField(verbose_name='¿es publico?',default=True, help_text='Bandera de si existe catálogo o si esta activo o no')
    isActive = models.BooleanField(help_text='Bandera de si existe catálogo o si esta activo o no')
    views = models.IntegerField(verbose_name='vistas',help_text='Número de veces que se ha consultado')
    modifications = models.IntegerField(verbose_name='modificaciones',help_text='Número de veces que se ha modificado algún registro')
    downloads = models.IntegerField(verbose_name='descargas',help_text='Número de veces que se ha descargado el catálogo')
    lastModifier = models.ForeignKey(User, verbose_name='ultimo en modificar',null=True, related_name='+', on_delete=models.SET_NULL)
    creationDate = models.DateTimeField(verbose_name='fecha creacion',auto_now_add=True, help_text="Fecha de creación")
    modificationDate = models.DateTimeField(verbose_name='fecha modificacion',auto_now_add=True, help_text="Fecha de modificación")
    class Meta(ModelBase.Meta):
        verbose_name = 'Catálogo Hive'
        verbose_name_plural = 'Catálogos Hive'
    def __str__(self):
        return "{0}".format(self.name)
    def getPermission(user):
        return True
    def getSchema(self, id):
        query = "SELECT * FROM {db}.{table} limit 1".format(
            db=settings.HIVE_DATABASE,
            table=HiveCatalogue.objects.get(id=self.get64Id(id))
        )
        cursor = Hive().getHiveConection()
        cursor.execute(query)
        return cursor.description
    def getUserCatalogues(self, user, queryset=None):
        if not queryset:
            queryset = HiveCatalogue.objects.all()
        return queryset.filter(
            Q(isPublic=True) |
            Q(administrators=user) |
            Q(superUsers=user) |
            Q(superGroups__in=user.groups.all()) |
            Q(users=user) |
            Q(groups__in=user.groups.all())
        ).distinct()
    def getData(self, id):
        query = "SELECT * FROM {db}.{table}".format(
            db = Hive().getDATABASE(),
            table = HiveCatalogue.objects.get(id=self.get64Id(id)).catalogue
        )
        return json.dumps(Hive().makeHiveQuery(query), cls=DjangoJSONEncoder)