from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Client(models.Model):
    email = models.EmailField(unique=True, max_length=100)

class Plate(models.Model):
    client = models.ForeignKey("Client", on_delete=models.CASCADE)
    registration = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r'^\d{2}[A-Z]{2}\d{2}$|^\d{2}-\d{2}-[A-Z]{2}$',
                message='Enter a valid license plate registration number in the format "00AA00" or "00-00-AA".',
                code="invalid_registration",
            ),
        ],)

    class Meta:
        unique_together = [["client", "registration"]]