from django import forms
from .models import Idea, Content, MediaFile

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = ['title', 'description', 'category', 'platform', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
            'description': forms.Textarea(attrs={'class': 'form-input w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500', 'rows': 4}),
            'category': forms.TextInput(attrs={'class': 'form-input w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
            'platform': forms.Select(attrs={'class': 'form-select w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
            'priority': forms.NumberInput(attrs={'class': 'form-input w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500'}),
        }

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['idea', 'script_text', 'video_file', 'thumbnail', 'status', 'publish_date']

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['file', 'file_type']
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-input w-full'}),
            'file_type': forms.Select(attrs={'class': 'form-select w-full rounded-md border-gray-300 shadow-sm'}),
        }
