from django.contrib import admin

from library.genre.models import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'slug']
    list_filter = ['type']
    search_fields = ['type']
    prepopulated_fields = {'slug': ('type',)}
    ordering = ['type']
    fieldsets = (
        ('Info', {'fields': ('type', 'description', 'slug')}),
    )
    readonly_fields = ('created', 'updated', 'slug')


