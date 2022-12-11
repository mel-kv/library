from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from library.author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death', 'slug']
    list_filter = ['first_name', 'last_name', 'date_of_birth']
    search_fields = ['first_name', 'last_name', 'date_of_birth', 'result__book_author']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}
    ordering = ['first_name', 'last_name']
    fieldsets = (
        (
        _('Personal info'), {'fields': ('first_name', 'last_name', 'date_of_birth', 'photo', 'date_of_death', 'slug')}),
    )
    readonly_fields = ('created', 'updated')
    date_hierarchy = 'date_of_birth'
