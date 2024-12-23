from django import forms
from .models import FeatureFile, PredictionFile

class FeatureFileForm(forms.ModelForm):
    class Meta:
        model = FeatureFile
        fields = ['file']

class PredictionFileForm(forms.ModelForm):
    class Meta:
        model = PredictionFile
        fields = ['file']
