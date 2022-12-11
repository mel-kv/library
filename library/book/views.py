from django.views import generic

from library.book.models import Book


class BookCreateView(generic.CreateView):
    model = Book
    template_name = "books/create.html"


class BookDetailsView(generic.DetailView):
    model = Book
    template_name = "books/details.html"


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = "books/edit.html"


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = "books/delete.html"


class BookListDisplayView(generic.ListView):
    model = Book
    template_name = "books/list_all.html"
