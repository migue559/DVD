
from django.contrib.auth.models import AbstractUser
#from django.conf import settings
from .modelsBase import *

class User(AbstractUser, ModelBase):
    pass
    class Meta():
        pass

#class Hive(ModelBase):
#    pass
#    def getHiveConection(self):
#        return hive.connect(
#            host=settings.HIVE_HOST,
#            port=settings.HIVE_PORT,
#            database=settings.HIVE_DATABASE,
#            username=settings.HIVE_USERNAME,
#            password=settings.HIVE_PASSWORD,
#            auth='CUSTOM').cursor()
#    def getDATABASE(self):
#        return settings.HIVE_DATABASE
#    def makeHiveQuery(self, query=None):
#        cursor = self.getHiveConection()
#        cursor.execute(query)
#        return cursor.fetchall()
