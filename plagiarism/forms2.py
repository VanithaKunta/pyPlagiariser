from django.forms import ModelForm
from django import forms
from plagiarism.models import File1,File2
class FilesCreate2(ModelForm):
    class Meta:
        model=File2
        exclude=()
        widgets={'secondfile':forms.Textarea(attrs={'cols':50,'rows':50})}