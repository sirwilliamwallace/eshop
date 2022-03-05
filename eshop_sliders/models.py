import os
from django.db import models


def get_filename_ext(filepath):
    """
    Get filename and extension from filepath
    """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


# End of get_filename_ext
def upload_image_path(instance, filename):
    """
    Upload image to path
    """
    name, ext = get_filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f"sliders/{final_name}"


# Create your models here.
class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    link = models.CharField(max_length=200, verbose_name='لینک')
    description = models.TextField(verbose_name='توضیحات')
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True,
                              verbose_name='تصویر')  # upload_to=upload_image_path is a function that will be called when the image is uploaded to the server and it will return the path to the image

    # Meta class for Product model to set the name of the model in the admin panel
    class Meta:
        """
        Meta class for Product model to set the name of the model in the admin panel
        """
        verbose_name = "اسلایدر"
        verbose_name_plural = "اسلایدر ها"

    def __str__(self):
        return self.title
