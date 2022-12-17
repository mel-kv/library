from django.shortcuts import redirect
from django.urls import reverse_lazy

from library.author.models import Author
from django.views import generic

from library.book_series.models import BookSeries
from library.mixin import StaffRequiredMixin


class BookSeriesCreateView(StaffRequiredMixin, generic.CreateView):
    model = BookSeries
    fields = '__all__'
    template_name = "series/create.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('series:details', kwargs={'slug': created_object.slug})

    def handle_no_permission(self):
        return redirect('index')


class BookSeriesDetailsView(generic.DetailView):
    model = BookSeries
    fields = '__all__'
    template_name = "series/details.html"


class BookSeriesUpdateView(StaffRequiredMixin, generic.UpdateView):
    model = BookSeries
    fields = '__all__'
    template_name = "series/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('series:details', kwargs={'slug': created_object.slug})

    def handle_no_permission(self):
        return redirect('index')


class BookSeriesDeleteView(StaffRequiredMixin, generic.DeleteView):
    model = BookSeries
    template_name = "series/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('series:all')

    def handle_no_permission(self):
        return redirect('index')


class BookSeriesListDisplayView(generic.ListView):
    model = BookSeries
    fields = '__all__'
    template_name = "series/list_all.html"
