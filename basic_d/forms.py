from django import forms

class EntryForm(forms.Form):
        name = forms.CharField(max_length=100)
        date = forms.DateTimeField(label='YYYY-MM-DD',
                  widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
        description = forms.CharField()
