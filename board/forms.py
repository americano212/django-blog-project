from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CreateBlog(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','content','tags']

        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'title_box', 'placeholder': '제목을 입력하세요.'}
            ),
            'description': forms.TextInput(
                attrs={'class': 'description_box', 'placeholder': '간단히 한문장으로 요약해주세요'}
            ),
            'tags': forms.TextInput(
                attrs={'class':'tags_box','placeholder':'태그'}
            ),
            'body': forms.CharField(widget=CKEditorUploadingWidget()),
        }
