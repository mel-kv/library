from django.urls import path, include

from library.publisher import views

app_name = 'publishers'
urlpatterns = [
    path('create/', views.PublisherCreateView.as_view(), name='create'),
    path('', views.PublisherListView.as_view(), name='all'),
    path('<slug:slug>/', include([
        path('', views.PublisherDetailView.as_view(), name='details'),
        path('edit/', views.PublisherUpdateView.as_view(), name='edit'),
        path('delete/', views.PublisherDeleteView.as_view(), name='delete')])),

]
