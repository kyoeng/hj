from turtle import title
from django.db import models

# Create your models here.

class Board(models.Model):
    title                                   = models.CharField(max_length=200, verbose_name='제목')
    content                                 = models.TextField(verbose_name='내용')
    created_at                              = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at                              = models.DateTimeField(auto_now=True, verbose_name='최종 수정일')
    board_name                              = models.CharField(max_length=50, default='notice', verbose_name='게시판 이름')
    hits                                    = models.PositiveIntegerField(default=0, verbose_name='조회수')
    delYn                                   = models.PositiveIntegerField(default=0, verbose_name='삭제여부')

    def __str__(self):
        return self.title