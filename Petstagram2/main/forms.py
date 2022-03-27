from django import forms

from Petstagram2.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from Petstagram2.main.models import Pet




class CreatePetForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        pet = super().save(commit=False)
        pet.user = self.user
        if commit:
            pet.save()
        return pet

    class Meta:
        model = Pet
        fields = ('name', 'type', 'date_of_birth')
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name'
                }
            ),
        }


class EditPetForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Pet
        exclude = ('user_profile',)
        widgets = {
            'name':forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name'
                }
            ),
        }


class DeletePetForm(forms.ModelForm, BootstrapFormMixin, DisabledFieldsFormMixin):
    disabled_fields = ('name', )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_form()

    class Meta:
        model = Pet
        exclude = ('user_profile',)

    def save(self, commit= True):
        self.instance.delete()
        return self.instance