from django.contrib import admin

from library.book_series.models import BookSeries


@admin.register(BookSeries)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    list_filter = ['name', 'author']
    search_fields = ['name', 'author']
    ordering = ['name', ]
    readonly_fields = ('slug',)
