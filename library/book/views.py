from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.urls import reverse_lazy
from django.views import generic

from library.book.models import Book


class BookCreateView(generic.CreateView):
    model = Book
    fields = '__all__'
    template_name = "books/create.html"

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['originally_published'].widget = DatePickerInput()
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
    fields = '__all__'
    template_name = "books/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('books:details', kwargs={'slug': created_object.slug})


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

