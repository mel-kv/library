from django.urls import path, include

from library.app_users import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='sign up'),
    path('signin/', views.SignInView.as_view(), name='sign in'),
    path('signout/', views.SignOutView.as_view(), name='sign out'),
    path('<slug:slug>/', include([

        path('', views.ProfileDetailsView.as_view(), name='details'),
        path('edit/', views.ProfileEditView.as_view(), name='edit'),
        path('delete/', views.ProfileDetailsView.as_view(), name='delete')])),
]
