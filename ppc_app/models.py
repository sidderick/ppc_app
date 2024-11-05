# models.py

from django.db import models
from datetime import timedelta, datetime, date


class PersonDetails(models.Model):
    userID = models.AutoField(primary_key=True, editable=False)
    nhsNumber = models.CharField(max_length=10, null=False)
    firstName = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    dateOfBirth = models.DateField(null=False)
    email = models.EmailField(null=False)

    def __str__(self):
        return str(self.userID)


class CertificateDetails(models.Model):
    certNumber = models.AutoField(primary_key=True)
    userID = models.ForeignKey(PersonDetails, on_delete=models.CASCADE)
    certType_choices = [
        ('ppc', 'PPC'),
        ('matex', 'Matex'),
    ]
    certType = models.CharField(max_length=5, choices=certType_choices, null=False)
    exempt = models.BooleanField(default=False, null=False)
    datePurchased = models.DateField(null=False)
    expiryDate = models.DateField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.pk:
            self.expiryDate = self.datePurchased + timedelta(days=365)
            if self.expiryDate > date.today():
                self.exempt = True
            else:
                self.exempt = False
        super().save(*args, **kwargs)
