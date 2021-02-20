from django.db import models

# Create your models here.

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=124, null=False, blank=False)
    email = models.CharField(max_length=124, null=False, blank=False)
    subject = models.CharField(max_length=12, null=True, blank=True)
    message = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=True , null=True, blank=True)

    def __str__(self):
        return self.name


class Career(models.Model):
    selected = models.CharField(max_length=124, null=False, blank=False, verbose_name='Position')
    firstName = models.CharField(max_length=124, null=False, blank=False)
    lastName = models.CharField(max_length=124, null=False, blank=False)
    email = models.CharField(max_length=124, null=False, blank=False)
    phone = models.CharField(max_length=15, null=False, blank=False)
    employment = models.CharField(max_length=124, null=False, blank=False)
    experience = models.CharField(max_length=124, null=False, blank=False)
    date_applied = models.DateField(auto_now_add=True,null=True, blank=True )
    letter = models.TextField(null=False, blank=False)
    file = models.FileField(upload_to='documents', max_length=100, blank=True)


    def __str__(self):
        return self.firstName