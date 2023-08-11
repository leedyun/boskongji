from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)  # 문자를 담은 필드
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)  # 월,일,시,분,초까지 기록할 수 있게 해주는 필드를 만들 때 사용
    updated_at = models.DateTimeField(auto_now=True)
    # author : 추후 작성 예정

    def __str__(self):
        return f'[{self.pk}] {self.title}'

# Create your models here.
