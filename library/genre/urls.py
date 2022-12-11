from django.urls import path, include

from library.genre import views

app_name = 'genres'


urlpatterns = [
    path('create/', views.GenreCreateView.as_view(), name='create'),
    path('<slug:slug>/', include([
        path('', views.GenreDetailsView.as_view(), name='details'),
        path('edit/', views.GenreUpdateView.as_view(), name='edit'),
        path('delete/', views.GenreDeleteView.as_view(), name='delete')])),
]
