from django.db import models

# django 모델 상속받음
class Review(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    