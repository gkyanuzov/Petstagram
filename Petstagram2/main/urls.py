from django.urls import path

from Petstagram2.main.views.generic_views import HomeView, DashboardView
from Petstagram2.main.views.pets_views import CreatePetView, EditPetView,DeletePetView
from Petstagram2.main.views.photo_views import PetPhotoDetailsView, like_pet_photo, \
    CreatePetPhotoView, EditPetPhotoView


urlpatterns = (
    path('', HomeView.as_view(), name ='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('photo/details/<int:pk>/', PetPhotoDetailsView.as_view(), name='photo details'),
    path('photo/like/<int:pk>/',like_pet_photo, name = 'like pet photo'),



    path('pet/create/', CreatePetView.as_view(), name='create pet'),
    path('pet/edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    path('pet/delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),

    path('photo/add/', CreatePetPhotoView.as_view(), name='create photo'),
    path('photo/edit/<int:pk>', EditPetPhotoView.as_view(), name='edit photo'),

)