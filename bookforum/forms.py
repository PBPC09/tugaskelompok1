from django.forms import ModelForm
from bookforum.models import ForumHead, ForumComment

class FormPertanyaan(ModelForm):
    class Meta:
        model = ForumHead
        fields = ["title", "question", "book"]


class FormJawaban(ModelForm):
    class Meta:
        model = ForumComment
        fields = ["answer"]