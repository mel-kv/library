from django.urls import reverse_lazy

from library.author.models import Author
from django.views import generic
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput


class AuthorCreateView(generic.CreateView):
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'image', 'about_info')
    model = Author
    template_name = "authors/create.html"

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['date_of_birth'].widget = DatePickerInput()
        form.fields['date_of_death'].widget = DatePickerInput()

        return form

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('authors:details', kwargs={'slug': created_object.slug})


class AuthorDetailsView(generic.DetailView):
    model = Author
    fields = '__all__'
    template_name = "authors/details.html"


class AuthorUpdateView(generic.UpdateView):
    model = Author
    fields = '__all__'
    template_name = "authors/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('authors:details', kwargs={'slug': created_object.slug})


class AuthorDeleteView(generic.DeleteView):
    model = Author
    template_name = "authors/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('authors:all')


class AuthorListDisplayView(generic.ListView):
    model = Author
    fields = '__all__'
    template_name = "authors/list_all.html"
