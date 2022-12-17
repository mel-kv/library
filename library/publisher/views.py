from django.urls import reverse_lazy
from django.views import generic

from library.publisher.models import Publisher


class PublisherCreateView(generic.CreateView):
    model = Publisher
    fields = '__all__'

    template_name = "publishers/create.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('publishers:details', kwargs={'slug': created_object.slug})


class PublisherDetailView(generic.DetailView):
    model = Publisher
    fields = '__all__'
    template_name = "publishers/details.html"


class PublisherUpdateView(generic.UpdateView):
    model = Publisher
    fields = '__all__'
    template_name = "publishers/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('publishers:details', kwargs={'slug': created_object.slug})


class PublisherDeleteView(generic.DeleteView):
    model = Publisher
    template_name = "publishers/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('publishers:all')


class PublisherListView(generic.ListView):
    model = Publisher
    fields = '__all__'
    template_name = "publishers/list_all.html"
