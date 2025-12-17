from django.shortcuts import render
from django.http import HttpResponse
from .forms import MeditationForm
from .utils import generate_meditation_script, generate_audio
import asyncio

def index(request):
    form = MeditationForm()
    return render(request, 'trainer/index.html', {'form': form})

async def generate(request):
    if request.method == 'POST':
        form = MeditationForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['mood']
            voice = form.cleaned_data['voice']
            
            # Generate script
            script = await generate_meditation_script(mood)
            
            # Generate audio
            audio_url = await generate_audio(script, voice)
            
            return render(request, 'trainer/result.html', {
                'script': script,
                'audio_url': audio_url,
                'mood': mood
            })
    return HttpResponse("Invalid request", status=400)
