from django.views import generic
from django.views.generic import DetailView

from library.genre.models import Genre


class GenreCreateView(generic.CreateView):
    model = Genre
    template_name = "genres/create.html"


class GenreDetailsView(generic.DetailView):
    model = Genre
    template_name = "genres/details.html"


class GenreUpdateView(generic.UpdateView):
    model = Genre
    template_name = "genres/edit.html"


class GenreDeleteView(generic.DeleteView):
    model = Genre
    template_name = "genres/delete.html"

