from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='purchase_orders')
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default='pending')
    quality_rating = models.FloatField(blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(5)])
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='historical_performances')
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    quality_rating_avg = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
