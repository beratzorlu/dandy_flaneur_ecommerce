from django.db import models
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    upc = models.CharField(max_length=50, null=True, blank=True)  # universal product code
    artist = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=254, unique=False, null=True, blank=True)
    name = models.CharField(max_length=254, unique=True, null=True, blank=True)
    description = models.TextField()
    has_dimentions = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.rating is not None and (self.rating < 0 or self.rating > 5):
            raise ValidationError("Rating value must be between 0 and 5")

    def save(self, *args, **kwargs):
        try:
            self.full_clean()
            super().save(*args, **kwargs)
        except ValidationError as e:
            messages.error(None, e.message)
