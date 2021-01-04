from django.urls import path
from .views import UserCreateView, UserEditView, PasswordsChangeView, PasswordSuccessView, ProfileDetailView, ProfileUpdateView, ProfileCreateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name="registration/change-password.html"), name='password'),
    path('password/', PasswordsChangeView.as_view(), name='password'),
    path('password_success/', PasswordSuccessView.as_view(), name='password_success'),
    path('<int:pk>/profile/', ProfileDetailView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile/', ProfileUpdateView.as_view(), name='edit_profile_page'),
    path('create_profile/', ProfileCreateView.as_view(), name='create_user_profile_page'),
]
