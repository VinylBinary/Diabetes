from django.shortcuts import render, redirect
from .forms import dataForm
import librosa
import tensorflow as tf
import numpy as np
def features_extractor(file):
    # load the audio file
    x, sample_rate = librosa.load(file, res_type='kaiser_fast')
    # extract features from the audio
    mfcc = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=50).T, axis=0)
    
    return mfcc
# Create your views here.

def predict(request):
    if request.method == "POST":
        f = dataForm(request.POST, request.FILES)
        if f.is_valid():
            print('done')
            f.save()
            try:
                features = features_extractor(f.cleaned_data['audio'])
                return render(request, 'result.html', {"result": "Diabetic"})
            except:
                # return redirect(result, {"result" : "Non-Diabetic"})
                return render(request, 'result.html', {"result": "Non-Diabetic"})
            
    else:
        f = dataForm()
    return render(request, 'process.html', {"form":f})

