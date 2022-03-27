# from django.shortcuts import render, redirect
# from django.views.generic import DetailView
#
# fro
#
# # po-dobro, ama ako znaesh kvo praish
# def profile_action(request, form_class, success_url, instance, template_name):
#     if request.method == 'POST':
#         form = form_class(request.POST, instance=instance)
#         if form.is_valid():
#             form.save()
#             return redirect(success_url)
#     else:
#         form = form_class(instance=instance)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, template_name, context)
#
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
#
#
# #
# # def create_profile(request):
# #     return profile_action(request, ProfileForm, 'index', Profile(), 'profile_create.html')
# #
#
# def edit_profile(request):
#     profile = get_profile()
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')f
#     else:
#         form = EditProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'main/profile_edit.html', context)
#
#
# # def edit_profile(request):
# #     return profile_action(request, EditProfileForm, 'profile details', get_profile(), 'profile_edit.html')
#
#
# def delete_profile(request):
#     return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'main/profile_delete.html')
#
#
class ProfileDetailsView(DetailView):
    model = Profile
    template_name = 'main/profile_details.html'
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
            'is_owner':self.object.user_id == self.request.user.id,
            'pets': pets,
        })
        return context
#
# # def show_profile(request):
# #     profile = get_profile()
# #     pets = list(Pet.objects.filter(user=profile))
# #     pet_photos = PetPhoto.objects \
# #                     .filter(tagged_pets__user_profile=profile) \
# #                     .distinct()
# #     total_likes = sum(pp.likes for pp in pet_photos)
# #     total_images = len(pet_photos)
# #
# #     context = {
# #         'profile':profile,
# #         'total_likes': total_likes,
# #         'total_images': total_images,
# #         'pets': pets,
# #     }
# #     return render(request, 'main/profile_details.html', context)
# #
