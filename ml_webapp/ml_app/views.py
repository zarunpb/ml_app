from django.shortcuts import render,redirect

# Create your views here.
import pandas as pd
from .models import FeatureFile, MLResult, PredictionFile
from .forms import FeatureFileForm, PredictionFileForm
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model(request):
    if request.method == 'POST':
        form = FeatureFileForm(request.POST, request.FILES)
        if form.is_valid():
            feature_file = form.save()
            data = pd.read_excel(feature_file.file.path)
            X = data.iloc[:, :-1]  # Features
            y = data.iloc[:, -1]  # Target
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)

            
            MLResult.objects.create(accuracy=accuracy)

            return redirect('train_model')

    else:
        form = FeatureFileForm()
        results = MLResult.objects.all()

    return render(request, 'train_model.html', {'form': form, 'results': results})

def predict(request):
    if request.method == 'POST':
        form = PredictionFileForm(request.POST, request.FILES)
        if form.is_valid():
            prediction_file = form.save()
            data = pd.read_excel(prediction_file.file.path)
            predictions = ["class1" for _ in range(len(data))]

            return render(request, 'predict.html', {'predictions': predictions})
    else:
        form = PredictionFileForm()

    return render(request, 'predict.html', {'form': form})
