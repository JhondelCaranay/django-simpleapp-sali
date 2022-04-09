from django import forms
from .models import Post


# class PostCreationForm(forms.Form):
#     title = forms.CharField(max_length=200)
#     author = forms.CharField(max_length=200)
#     content = forms.CharField(widget=forms.Textarea)

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'content', 'thumbnail']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'style': 'resize: vertical'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }

    # add form-control class to inputs
    # def __init__(self, *args, **kwargs):
    #     super(PostCreationForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field in self.fields:
    #         self.fields[field].widget.attrs.update({'class': 'form-control'})
