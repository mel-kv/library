from django.urls import path, include

from library.book import views

app_name = 'books'

urlpatterns = [
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('', views.BookListDisplayView.as_view(), name='all'),
    path('<slug:slug>/', include([
        path('', views.BookDetailsView.as_view(), name='details'),
        path('edit/', views.BookUpdateView.as_view(), name='edit'),
        path('delete/', views.BookDeleteView.as_view(), name='delete')])),
]