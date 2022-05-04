from django.db import models

class Category(models.Model):
    name = models.CharField('Category', max_length=150)
    description = models.TextField('Description')
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        verbouse_name = 'Category'
        verbouse_name_plural = 'Categories'