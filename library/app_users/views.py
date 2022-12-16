from django.contrib.auth import login, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from library.app_users import forms

UserModel = get_user_model()


class SignUpView(CreateView):
    template_name = 'lusers/sign_up.html'
    form_class = forms.SignUpForm
    extra_context = {'title': 'Sign Up'}

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('users:details', kwargs={'slug': created_object.slug})


class SignInView(LoginView):
    template_name = 'lusers/sign_in.html'
    extra_context = {'title': 'Sign In'}

    def get_success_url(self):
        return reverse_lazy("index")


class SignOutView(LogoutView):
    template_name = 'lusers/sign_out.html'
    extra_context = {'title': 'Sign Out'}

    def get_success_url(self):
        return reverse_lazy("index")


class UsersList(LoginRequiredMixin, ListView):
    model = UserModel
    template_name = 'lusers/list_all.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        return context


class ProfileDetailsView(DetailView):
    template_name = 'lusers/details.html'
    model = UserModel
    fields = '__all__'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def get_object(self):
        return self.request.user


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = UserModel
    template_name = 'lusers/edit.html'
    context_object_name = 'user'
    fields = '__all__'

    def get_success_url(self):
        created_object = self.object
        return reverse_lazy('users:details', kwargs={'slug': created_object.slug})


class ProfileDeleteView(DeleteView):
    model = UserModel
    template_name = 'lusers/delete.html'
    next_page = reverse_lazy('index')
    success_url = reverse_lazy('index')

    def post(self, *args, pk):
        self.request.user.delete()
