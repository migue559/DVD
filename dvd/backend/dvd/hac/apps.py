from dvd.core.apps import *
from django.conf import settings


print("settings.DEBUG")
print(settings.DEBUG)

class HacConfig(AppConfig):
    name = "dvd.hac"
    verbose_name = ("Catalogos")
    def ready(self):
        import dvd.hac.signals
        if 1==1:#try:
            if settings.DEBUG:
                from .models import HiveCatalogue
                from dvd.core.models import User
                import random
                catalogues = [
                    'cat_dummy_aseguradora',
                    'cat_dummy_banco',
                    'cat_dummy_cedis',
                    'cat_dummy_colores',
                    'cat_dummy_escuelas',
                    'cat_dummy_estadocivil',
                    'cat_dummy_genero',
                    'cat_dummy_instituciones',
                    'cat_dummy_pais',
                    'cat_dummy_proveedor',
                ]
                if not HiveCatalogue.objects.all():
                    print("yei")
                    for catalogue in catalogues:
                        hiveCatalogue = HiveCatalogue.objects.create(
                            name = catalogue,
                            description = catalogue,
                            catalogue = catalogue,
                            isActive = True,
                            views = random.randint(100, 999999999),
                            modifications = random.randint(100, 999999999),
                            downloads = random.randint(100, 999999999),
                            lastModifier = User.objects.all().first()
                        )
                        hiveCatalogue.administrators.add(User.objects.all().first())
        #except:
        #    pass

