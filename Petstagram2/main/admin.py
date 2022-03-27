from django.contrib import admin

from Petstagram2.main.models import  Pet, PetPhoto

class PetInlineAdmin(admin.StackedInline):
    model = Pet



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass