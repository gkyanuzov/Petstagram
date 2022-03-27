import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram2.main.validators import only_letters_validator, image_max_size_validator

UserModel = get_user_model()



class Pet(models.Model):
    NAME_MAX_LEN = 30

    CAT = 'Cat'
    DOG = 'Dog'
    BUNNY = 'Bunny'
    PARROT = 'Parrot'
    FISH = 'Fish'
    OTHER = 'Other'
    TYPES = [(x, x) for x in (CAT, DOG, BUNNY, PARROT, FISH, OTHER)]

    name = models.CharField(
        max_length=NAME_MAX_LEN,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    # One-To-Many Relation - Edin User ima Mnogo petove
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # image_max_size_validator(5),
        )
    )

    # edin pet moje da e v mnogo snimki, i v edna snimka moje da ima mnogo pets
    tagged_pets = models.ManyToManyField(
        Pet,
        #validate at least one pet
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )