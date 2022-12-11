from django.contrib import admin

from django.utils.translation import gettext_lazy as _

from library.app_users.models import LUser


@admin.register(LUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth', 'slug',)
    list_filter = ['is_staff', 'is_superuser', 'groups', 'first_name', 'last_name', 'date_of_birth']
    fieldsets = (
        ('Credentials', {'fields': ('email', 'password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth',)}),
        # (_('Library info'), {'fields': ('library_card_number',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions',)}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    date_hierarchy = 'date_joined'
    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('date_joined', 'is_staff', 'email',)
    readonly_fields = ('date_joined', 'last_login', 'slug',)


