from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from Petstagram2.accounts.views import UserLoginView, ProfileDetailsView, UserRegisterView, EditProfileView, \
    ChangeUserPasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('<int:pk>/', ProfileDetailsView.as_view(), name='profile'),
    path('register/', UserRegisterView.as_view(), name='create profile'),
    # path('profile/edit/', edit_profile, name='edit profile'),
    # path('profile/delete/', delete_profile, name='delete profile'),
    path('edit-password/', ChangeUserPasswordView.as_view(), name = 'change password'),
    path('change-pass-done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='pass change done'),

)