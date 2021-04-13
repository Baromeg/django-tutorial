from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10000, decimal_places=2)
    # blank=False === to required - # null=False === is required in the database
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=False)  # null=True, default=True
    def get_absolute_url(self):
        return f'/products/{self.id}'
    