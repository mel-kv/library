from library.author.models import Author
from django.views import generic


class AuthorCreateView(generic.CreateView):
    model = Author
    template_name = "authors/create.html"


class AuthorDetailsView(generic.DetailView):
    model = Author
    template_name = "authors/details.html"


class AuthorUpdateView(generic.UpdateView):
    model = Author
    template_name = "authors/edit.html"


class AuthorDeleteView(generic.DeleteView):
    model = Author
    template_name = "authors/delete.html"
