from django.db import models

# Create your models here.


class FeatureFile(models.Model):
    file = models.FileField(upload_to='features/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class PredictionFile(models.Model):
    file = models.FileField(upload_to='predictions/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MLResult(models.Model):
    accuracy = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
