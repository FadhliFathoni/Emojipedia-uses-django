from django import forms
from .models import EmojiModels
    
class EmojiForm(forms.ModelForm):
    class Meta:
        model = EmojiModels
        fields = ("__all__")

    def clean_nama(self):
        data = self.cleaned_data["nama"]
        return data