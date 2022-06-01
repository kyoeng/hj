from django.contrib import admin
from board.models import Board
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Board)
class BoardAdmin(SummernoteModelAdmin):
    summernote_fields                       = ('content')
    list_display                            = (
      'id',
      'board_name',
      'title',
      'content',
      'hits',
      'created_at',
      'updated_at',
      'delYn'
    )
    list_display_links                      = list_display