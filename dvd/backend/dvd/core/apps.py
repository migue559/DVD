from django.apps import AppConfig
from django.conf import settings


class CoreConfig(AppConfig):
    name = "dvd.core"
    verbose_name = ("CORE")
    def ready(self):
        import dvd.core.signals
        try:
            from .models import User        
            def createFirstUser():
                if not User.objects.all().first():
                    user = User.objects.create(
                        username=settings.USERNAME,
                        is_superuser=True,
                        is_staff=True
                    )
                    user.set_password(settings.PASSWORD)
                    user.save()
            createFirstUser()
        except:
            pass
