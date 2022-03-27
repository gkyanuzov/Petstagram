from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from Petstagram2.accounts.models import Profile
from Petstagram2.common.helpers import BootstrapFormMixin
from Petstagram2.main.models import PetPhoto


class ProfileForm(UserCreationForm, BootstrapFormMixin):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )

    picture = forms.URLField()

    date_of_birth = forms.DateField()

    decsription = forms.CharField(
        widget=forms.Textarea,
    )

    email = forms.EmailField()

    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            decsription=self.cleaned_data['decsription'],
            email=self.cleaned_data['email'],
            gender=self.cleaned_data['gender'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2' ,'first_name', 'last_name', 'picture', 'decsription')
        widgets = {'first_name': forms.TextInput(
            attrs={
                'placeholder': 'Enter first name'
            }
        ), 'last_name': forms.TextInput(
            attrs={
                'placeholder': 'Enter last name'

            }
        ), 'picture': forms.TextInput(
            attrs={
                'placeholder': 'Enter URL'
            }
        ),
        }


class EditProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {'first_name': forms.TextInput(
            attrs={
                'placeholder': 'Enter first name'
            }
        ), 'last_name': forms.TextInput(
            attrs={
                'placeholder': 'Enter last name'

            }
        ), 'picture': forms.TextInput(
            attrs={
                'placeholder': 'Enter URL'
            }
        ), 'email': forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email'
            }
        ), 'decsription': forms.Textarea(
            attrs={
                'placeholder': 'Enter descritpion',
                'rows': 3
            }
        ), 'date_of_birth': forms.DateInput(
            attrs={
                'min': '1920-01-01',
            }
        )

        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        pets = list(self.instance.pet_set.all())
        # should be done with singal
        PetPhoto.objects.filter(tagged_pets__in=pets).delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Profile
        fields = ()
