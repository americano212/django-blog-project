from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','slug','description','content','tags']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요.'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }
