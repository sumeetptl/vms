from django.db import models


class StatusChoices(models.TextChoices):
    Pending = 'Pending'
    Completed = 'Completed'
    Canceled = 'Canceled'


# Create your models here.
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, null=False)
    vendor = models.ForeignKey("vendor.Vendor", on_delete=models.CASCADE, related_name="purchase")
    order_date = models.DateTimeField(auto_now=True, auto_now_add=False)
    delivery_date = models.DateTimeField(null=True,auto_now=False,auto_now_add=False)
    items = models.JSONField()
    quantity = models.IntegerField(max_length=50)
    status = models.CharField(choices=StatusChoices,max_length=30)
    quality_rating = models.FloatField(default=7.0)
    issue_date = models.DateTimeField(null=True,auto_now=False, auto_now_add=False)
    acknowledgement_date = models.DateTimeField(null=True,auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.po_number

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
