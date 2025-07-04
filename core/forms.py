from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']

from .models import RecentWork
from django import forms

class RecentWorkForm(forms.ModelForm):
    class Meta:
        model = RecentWork
        fields = ['title', 'description']

from .models import Client

class ClientIntakeForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['created_at']
        widgets = {
            'proposed_date': forms.DateInput(attrs={'type': 'date'}),
        }

from .models import WorkVideo

class WorkVideoForm(forms.ModelForm):
    class Meta:
        model = WorkVideo
        fields = ['title', 'platform', 'video_url']
        widgets = {
            'video_url': forms.URLInput(attrs={
                'placeholder': 'https://www.tiktok.com/@username/video/1234567890'
            }),
        }
        help_texts = {
            'video_url': 'Paste the full video link (not a short link). For TikTok, use https://www.tiktok.com/@.../video/ID',
        }

from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}),
        }