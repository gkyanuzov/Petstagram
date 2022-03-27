from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from Petstagram2.accounts.forms import ProfileForm, DeleteProfileForm
from Petstagram2.accounts.models import Profile
from Petstagram2.common.view_mixins import RedirectToDashboard
from Petstagram2.main.models import Pet, PetPhoto
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView


class UserRegisterView(RedirectToDashboard, CreateView):
    form_class = ProfileForm
    template_name = 'main/../../templates/accounts/profile_create.html'
    success_url = reverse_lazy('dashboard')


class UserLoginView(LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('dashboard')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().success_url()


class EditProfileView:
    pass


class ChangeUserPasswordView(PasswordChangeView):
    template_name = 'accounts/change_pass.html'
    pass


#
# def create_profile(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = ProfileForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'main/profile_create.html', context)


# def edit_profile(request):
#     return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'profile_edit.html')


# def delete_profile(request):
# return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')


class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'main/../../templates/accounts/profile_details.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pets = list(Pet.objects.filter(user_id=self.object.user_id))

        pet_photos = PetPhoto.objects \
            .filter(tagged_pets__in=pets) \
            .distinct()

        total_likes = sum(pp.likes for pp in pet_photos)
        total_images = len(pet_photos)

        context.update({
            'total_likes': total_likes,
            'total_images': total_images,
            'is_owner': self.object.user_id == self.request.user.id,
            'pets': pets,
        })
        return context

# def show_profile(request):
#     profile = get_profile()
#     pets = list(Pet.objects.filter(user=profile))
#     pet_photos = PetPhoto.objects \
#                     .filter(tagged_pets__user_profile=profile) \
#                     .distinct()
#     total_likes = sum(pp.likes for pp in pet_photos)
#     total_images = len(pet_photos)
#
#     context = {
#         'profile':profile,
#         'total_likes': total_likes,
#         'total_images': total_images,
#         'pets': pets,
#     }
#     return render(request, 'main/profile_details.html', context)
#
