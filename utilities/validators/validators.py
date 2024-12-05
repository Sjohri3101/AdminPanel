from django.core.validators import URLValidator, RegexValidator
from django.core.exceptions import ValidationError
import os


alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed')

def image_file_validator(value):
    ext = os.path.splitext(value.name)[1]
    limit = 2 * 1024 * 1024 
    valid_extensions = ['.jpg','.jpeg','.svg','.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension for image.')
    elif value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')