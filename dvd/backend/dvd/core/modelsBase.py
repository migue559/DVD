from django.db import models
import base64

APP = 'core'

########################################################################################
class ModelBase(models.Model):
    active = models.BooleanField(default=True, editable=False)
    class Meta():
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ['-id']
        abstract = True
    def get64Id(self, id):
        type_, id_ = base64.b64decode(id).decode('utf-8').split(':')
        return int(id_)
    def get64Object(self, id):
        type_, id_ = base64.b64decode(id).decode('utf-8').split(':')
        return self.__class__.objects.get(id=id_)
