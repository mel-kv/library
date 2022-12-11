from django.contrib import admin

from library.book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title',  'originally_published', 'publisher', ]
    list_filter = ['title', 'author', 'originally_published', 'genres', 'publisher']
    search_fields = ['title', 'author', 'originally_published', 'genres', 'publisher']
    ordering = ['title', 'author', 'originally_published', 'genres', 'publisher']
    date_hierarchy = 'originally_published'
    readonly_fields = ('created', 'updated', 'slug',)

