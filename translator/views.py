# views.py
from django.shortcuts import render
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import base64

def translate(request):
    translated_audio_base64 = None
    
    if request.method == 'POST':
        speech_text = request.POST.get('speech_text', '')  # Extract speech text from the POST request
        source_lang = request.POST.get('source_lang', 'en')  # Get selected source language
        dest_lang = request.POST.get('destination_lang', 'hi')  # Get selected destination language
        print(dest_lang, "Destination Language", source_lang)  # Debugging statement

        if speech_text:  # Check if speech_text is not empty
            # Translate text
            translator = Translator()
            translated_result = translator.translate(speech_text, src=source_lang, dest=dest_lang)
            print(translated_result)
            # Check if translation result is not None
            if translated_result:
                translated_text = translated_result.text

                # Convert translated text to speech
                translated_audio = gTTS(translated_text, lang=dest_lang)
                translated_audio.save('translated_audio.mp3')

                # Encode the translated audio file into base64 format
                with open('translated_audio.mp3', 'rb') as f:
                    encoded_audio = base64.b64encode(f.read()).decode('utf-8')
                    translated_audio_base64 = f"data:audio/mpeg;base64,{encoded_audio}"
    
    return render(request, 'home.html', {'translated_audio_base64': translated_audio_base64})
