from django.urls import path, include

from library.book_series import views

app_name = 'series'

urlpatterns = [
    path('create/', views.BookSeriesCreateView.as_view(), name='create'),
    path('', views.BookSeriesListDisplayView.as_view(), name='all'),
    path('<slug:slug>/', include([
        path('', views.BookSeriesDetailsView.as_view(), name='details'),
        path('edit/', views.BookSeriesUpdateView.as_view(), name='edit'),
        path('delete/', views.BookSeriesDeleteView.as_view(), name='delete')])),
]
