from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.urls import reverse_lazy
from django.views import generic

from library.book.forms import BookForm
from library.book.models import Book


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'image', 'author', 'genres',
              'publisher', 'pages', 'series_name',
              'volume_number', 'originally_published',
              'description']
    template_name = "books/create.html"

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['originally_published'].widget = DatePickerInput()
        form.fields['originally_published'].widget.attrs = {'placeholder': 'mm/dd/yyyy'}
        return form

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('books:details', kwargs={'slug': created_object.slug})


class BookDetailsView(generic.DetailView):
    model = Book
    fields = '__all__'
    template_name = "books/details.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'image', 'author', 'genres',
              'publisher', 'pages', 'series_name',
              'volume_number', 'originally_published',
              'description']

    template_name = "books/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('books:details', kwargs={'slug': created_object.slug})


class BookReaderView(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/reader.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('books:all')

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['date_checked_out'].widget = DatePickerInput()
        form.fields['date_to_return'].widget = DatePickerInput()
        form.fields['date_checked_out'].widget.attrs = {'placeholder': 'mm/dd/yyyy'}
        form.fields['date_to_return'].widget.attrs = {'placeholder': 'mm/dd/yyyy'}

        return form

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('books:all')


class BookListDisplayView(generic.ListView):
    model = Book
    template_name = "books/list_all.html"
    fields = '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()
        pattern = self.__get_pattern()

        if pattern:
            queryset = queryset.filter(title__icontains=pattern)
        queryset = queryset.order_by('title')
        return queryset

    def __get_pattern(self):
        pattern = self.request.GET.get('pattern', None)
        return pattern.lower() if pattern else None
