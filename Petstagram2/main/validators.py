from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError('Value must contain only letters!')

def image_max_size_validator(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {str(max_size)}')
    return validate