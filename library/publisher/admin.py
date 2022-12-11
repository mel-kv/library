from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from library.publisher.models import Publisher


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'year_founded']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['name', 'year_founded']

    fieldsets = (
        ('Credentials', {'fields': ('name', 'description', 'year_founded', 'slug')}),
    )
    date_hierarchy = 'created'
    readonly_fields = ('created', 'updated')
