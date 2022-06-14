# Created by Akash Tilak on 13.06.2022


# gave command "pip install SpeechRecognition" in Windows PowerShell
import speech_recognition as s_r

# Importing HttpResponse and render
from django.shortcuts import render


# from django.http import HttpResponse


# Make sure you use return keyword for sure.
def index(request):
    return render(request, 'index.html')


def submitquery(request):
    clientName = request.GET.get('fullname', 'anonymous')
    clientAge = request.GET.get('age', '0')
    clientEmail = request.GET.get('email', 'Error')
    clientPno = request.GET.get('pno', '0')
    clientQuery = request.GET.get('query', 'Error Query')
    params = {'name': clientName, 'age': clientAge, 'email': clientEmail, 'phone': clientPno, 'query': clientQuery}
    return render(request, 'submitted.html', params)

# def speechrecog(request):
# #might encounter with:  error: Microsoft Visual C++ 14.0 or greater is required. Get it with "Microsoft C++ Build Tools": https://visualstudio.microsoft.com/visual-cpp-build-tools/
#     r = s_r.Recognizer()
#     my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index
#     with my_mic as source:
#         print("Say now!!!!")
#         r.adjust_for_ambient_noise(source)  # reduce noise
#         audio = r.listen(source)  # take voice input from the microphone
#     print(r.recognize_google(audio))