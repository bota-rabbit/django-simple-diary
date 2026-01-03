from django.db import models
from django.urls import reverse

class Diary(models.Model):
    title = models.CharField("タイトル", max_length=200)
    body = models.TextField("本文")
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)

    # 更新後の移動先
    def get_absolute_url(self):
        return reverse('diary:detail', kwargs={'pk': self.pk})

    # Diary を取得するときは新しい順番に並べる
    class Meta:
        ordering = ["-created_at"]

    # 管理画面でオブジェクトではなく日本語表示にする
    def __str__(self):
        return self.title
