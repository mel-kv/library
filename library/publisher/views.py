from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from library.mixin import StaffRequiredMixin
from library.publisher.models import Publisher


class PublisherCreateView(StaffRequiredMixin, generic.CreateView):
    model = Publisher
    fields = '__all__'

    template_name = "publishers/create.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('publishers:details', kwargs={'slug': created_object.slug})

    def handle_no_permission(self):
        return redirect('index')


class PublisherDetailView(generic.DetailView):
    model = Publisher
    fields = '__all__'
    template_name = "publishers/details.html"


class PublisherUpdateView(StaffRequiredMixin, generic.UpdateView):
    model = Publisher
    fields = '__all__'
    template_name = "publishers/edit.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('publishers:details', kwargs={'slug': created_object.slug})

    def handle_no_permission(self):
        return redirect('index')


class PublisherDeleteView(StaffRequiredMixin, generic.DeleteView):
    model = Publisher
    template_name = "publishers/delete.html"

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('publishers:all')

    def handle_no_permission(self):
        return redirect('index')


class PublisherListView(generic.ListView):
    model = Publisher
    fields = '__all__'
    template_name = "publishers/list_all.html"
