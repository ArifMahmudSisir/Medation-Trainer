from django import forms

VOICE_CHOICES = [
    ('en-US-AriaNeural', 'Aria (US Female)'),
    ('en-US-GuyNeural', 'Guy (US Male)'),
    ('en-US-JennyNeural', 'Jenny (US Female)'),
    ('en-GB-SoniaNeural', 'Sonia (UK Female)'),
    ('en-GB-RyanNeural', 'Ryan (UK Male)'),
]

MOOD_CHOICES = [
    ('Stress', 'Stress'),
    ('Anxiety', 'Anxiety'),
    ('Sleep', 'Sleep'),
    ('Focus', 'Focus'),
    ('Gratitude', 'Gratitude'),
]

class MeditationForm(forms.Form):
    mood = forms.ChoiceField(choices=MOOD_CHOICES, widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'}))
    voice = forms.ChoiceField(choices=VOICE_CHOICES, initial='en-US-AriaNeural', widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'}))
