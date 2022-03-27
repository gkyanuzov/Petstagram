from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from Petstagram2.main.forms import CreatePetForm, EditPetForm, DeletePetForm


class CreatePetView(CreateView):
    template_name = 'main/pet_create.html'
    form_class = CreatePetForm
    success_url = reverse_lazy('dashboard')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs





class EditPetView(UpdateView):
    template_name = 'main/pet_edit.html'
    form_class = EditPetForm


class DeletePetView(DeleteView):
    template_name = 'main/pet_delete.html'
    form_class = DeletePetForm
