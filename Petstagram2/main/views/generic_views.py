from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from Petstagram2.common.view_mixins import RedirectToDashboard
from Petstagram2.main.models import PetPhoto


class DashboardView(ListView):
    model = PetPhoto
    template_name = 'main/dashboard.html'
    context_object_name = 'pet_photos'


#staroto e FBV, gornoto e ok

# def show_dashboard(request):
#     profile = get_profile()
#     # if not profile:
#     #     return redirect('401')
#     pet_photos = set(
#         PetPhoto.objects
#         .prefetch_related('tagged_pets') \
#         .filter(tagged_pets__user_profile=profile))
#
#     context = {
#         'pet_photos': pet_photos,
#     }
#
#     return render(request, 'main/dashboard.html', context)


#
# def show_home(request):
#     context = {
#         'hide_addition_nav_items': True,
#     }
#     return render(request, 'main/home_page.html', context)
# Ekvivalentno na dolnoto

class HomeView(TemplateView, RedirectToDashboard):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_addition_nav_items'] = True
        return context


