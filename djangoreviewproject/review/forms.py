from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        # 어떤 모델이랑 연결할건지 알려줌
        model = Review

        # 어떤 부분을 보여줄건지 지정
        fields = ('title', 'content')