from django import forms

class PostForm(forms.Form):
    title = forms.CharField(required=True,
            widget=forms.TextInput(attrs={'placeholder': 'Razmi', 'class': 'form-control'}))

    text = forms.CharField(required=True)

    def clean_title(self):
        data = self.cleaned_data['title']
        if 'razmi' in data:
            raise forms.ValidationError('Razmi not allowed')

        return data

    def clean(self):
        data = self.cleaned_data
        return data
