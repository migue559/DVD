from django.contrib import admin
#from .models import User
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from .forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext_lazy as _


User = get_user_model()
@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):    
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('username', 'email', 'is_superuser','last_login','is_active')
    list_filter = ('username', 'email')
    filter_horizontal = ('groups',)
    fieldsets = ((None, { 'fields': ('username', 'password', 'email', 'is_superuser','is_active', 'last_login')
        }),
        ('Adminstracion', {
            'fields': ('groups',)
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    




