from django.urls import path, include

from library.author import views

app_name = 'authors'
urlpatterns = [
    path('create/', views.AuthorCreateView.as_view(), name='create'),
    path('<slug:slug>/', include([
        path('', views.AuthorDetailsView.as_view(), name='details'),
        path('edit/', views.AuthorUpdateView.as_view(), name='edit'),
        path('delete/', views.AuthorDeleteView.as_view(), name='delete')])),
]
