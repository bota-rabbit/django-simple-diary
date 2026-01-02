from django.contrib import admin
from .models import Diary

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    ordering = ('-created_at',)    # 並び順を指定
    search_fields = ('title', 'body')    # 検索できるようにする
    list_filter = ('created_at',)    # 日付で絞り込み
