from django.db import models

class Diary(models.Model):
    title = models.CharField("タイトル", max_length=200)
    body = models.TextField("本文")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
