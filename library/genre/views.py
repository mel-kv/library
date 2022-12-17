from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from library.genre.models import Genre


class GenreCreateView(generic.CreateView):
    model = Genre
    fields = '__all__'
    template_name = "genres/create.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('genres:details', kwargs={'slug': created_object.slug})


class GenreDetailsView(generic.DetailView):
    model = Genre
    fields = '__all__'
    template_name = "genres/details.html"


class GenreUpdateView(generic.UpdateView):
    model = Genre
    fields = '__all__'
    template_name = "genres/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('genres:details', kwargs={'slug': created_object.slug})


class GenreDeleteView(generic.DeleteView):
    model = Genre
    template_name = "genres/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('genres:delete')


class GenreListView(generic.ListView):
    model = Genre
    fields = '__all__'
    template_name = "genres/list_all.html"
