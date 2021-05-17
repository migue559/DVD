from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from dvd.core.admin import *
from dvd.core.models import *
from .models import HiveCatalogue

@admin.register(HiveCatalogue)
class HiveCatalogueAdmin(admin.ModelAdmin):
    list_display = ('catalogue','name', 'isPublic', 'views','description')
    filter_horizontal = ('groups','superGroups','administrators', 'superUsers','users')
    list_filter = ('users','isPublic')
    fieldsets = (        (None, { 'fields': ('name','description',('isPublic','isActive'),('views','modifications','downloads'))
        }),
        ('Cambios', {
            'fields': ('lastModifier',)
        }),
        ('Adminstracion', {
            'fields': ('administrators','superUsers','users')
        }),
    )

admin.site.unregister(Group)
@admin.register(Group)
class CustomGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (        (None, { 'fields': ('name',)
        }),
    )
