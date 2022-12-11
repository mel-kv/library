from django.contrib import admin

from django.urls import path, include

from library.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('publishers/', include('library.publisher.urls', namespace='publishers')),
    path('authors/', include('library.author.urls', namespace='authors')),
    path('books/', include('library.book.urls', namespace='books')),
    path('genres/', include('library.genre.urls', namespace='genres')),
    path('profile/', include('library.app_users.urls', namespace='users')),

]
