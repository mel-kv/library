from django.urls import path

from library.publisher import views

app_name = 'publishers'
urlpatterns = [
    path('<slug:slug>/', views.PublisherDetailView.as_view(), name='details')

]
