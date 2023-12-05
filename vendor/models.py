from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=200, null=False)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
