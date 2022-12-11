from django.views import generic

from library.publisher.models import Publisher


class PublisherCreateView(generic.CreateView):
    model = Publisher
    template_name = "publishers/create.html"


class PublisherDetailView(generic.DetailView):
    model = Publisher
    template_name = "publishers/details.html"


class PublisherUpdateView(generic.UpdateView):
    model = Publisher
    template_name = "publishers/edit.html"


class PublisherDeleteView(generic.DeleteView):
    model = Publisher
    template_name = "publishers/delete.html"
