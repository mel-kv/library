from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.utils.translation import gettext_lazy as _

from library.app_users.forms import SignUpForm, LUserChangeForm
from library.app_users.models import LUser


@admin.register(LUser)
class LUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = LUserChangeForm
    model = LUser
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'is_staff', 'slug',)
    list_filter = ('email', 'first_name', 'last_name','is_staff', 'is_active', 'groups')
    fieldsets = (
        ('Credentials', {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth',)}),
        (_('Library info'), {'fields': ('library_card_number',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('date_joined', 'is_staff', 'email',)
    readonly_fields = ('date_joined', 'last_login', 'slug', 'library_card_number')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'password1', 'password2'),
        }),
    )
# list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth', 'slug',)
    # list_filter = ['is_staff', 'is_superuser', 'groups', 'first_name', 'last_name', 'date_of_birth']
