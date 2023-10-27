from django.forms import ModelForm
from bookforum.models import ForumHead, ForumComment

class FormPertanyaan(ModelForm):
    class Meta:
        model = ForumHead
        fields = ["title", "book", "question", ]


class FormJawaban(ModelForm):
    class Meta:
        model = ForumComment
        fields = ["answer"]