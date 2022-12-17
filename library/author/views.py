from django.shortcuts import redirect
from django.urls import reverse_lazy

from library.author.models import Author
from django.views import generic
from bootstrap_datepicker_plus.widgets import DateTimePickerInput, DatePickerInput

from library.mixin import StaffRequiredMixin


class AuthorCreateView(StaffRequiredMixin, generic.CreateView):
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'image', 'about_info')
    model = Author
    template_name = "authors/create.html"

    def get_form(self, **kwargs):
        form = super().get_form()
        form.fields['date_of_birth'].widget = DatePickerInput()
        form.fields['date_of_death'].widget = DatePickerInput()
        return form

    def handle_no_permission(self):
        return redirect('index')

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('authors:details', kwargs={'slug': created_object.slug})


class AuthorDetailsView(generic.DetailView):
    model = Author
    fields = '__all__'
    template_name = "authors/details.html"


class AuthorUpdateView(StaffRequiredMixin, generic.UpdateView):
    model = Author
    fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death', 'image', 'about_info')
    template_name = "authors/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('authors:details', kwargs={'slug': created_object.slug})

    def handle_no_permission(self):
        return redirect('index')


class AuthorDeleteView(StaffRequiredMixin, generic.DeleteView):
    model = Author
    template_name = "authors/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('authors:all')

    def handle_no_permission(self):
        return redirect('index')


class AuthorListDisplayView(generic.ListView):
    model = Author
    fields = '__all__'
    template_name = "authors/list_all.html"
