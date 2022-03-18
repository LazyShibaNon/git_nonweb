from django import forms
from .models import team_photo

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = team_photo
        fields = ('image',)
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
        }
