from django.apps import AppConfig

#class CoreConfig(AppConfig):
#    name = "hac.core"
#    verbose_name = ("CORE")
#    def ready(self):
#        import hac.core.signals
#        try:
#            from .models import User
#            from django.conf import settings
#            def createFirstUser():
#                if not User.objects.all().first():
#                    user = User.objects.create(
#                        username=settings.USERNAME,
#                        is_superuser=True,
#                        is_staff=True
#                    )
#                    user.set_password(settings.PASSWORD)
#                    user.save()
#            createFirstUser()
#        except:
#            pass
