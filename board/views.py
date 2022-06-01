from django.shortcuts import render
from django.views.generic import ListView

## 게시판 리스트
class IndexView(ListView):

    template_name                       = 'board/index.html'
    context_object_name                 = 'data'

    def get_queryset(self):
        return ''

    def get_context_data(self, **kwargs):
        context                         = super().get_context_data(**kwargs)
        return context


## 게시글 작성
class WriteView(ListView):
    template_name                       = 'board/write.html'
    context_object_name                 = 'data'

    def get_queryset(self):
        return ''

    def get_context_data(self, **kwargs):
        context                         = super().get_context_data(**kwargs)
        return context