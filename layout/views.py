from django.shortcuts import render
from django.views.generic import ListView

# Main
class MainView(ListView):

    template_name                       = 'layout/main.html'
    context_object_name                 = 'data'

    def get_queryset(self):
        return ''

    def get_context_data(self, **kwargs):
        context                         = super().get_context_data(**kwargs)
        context['css_file']             = 'inc/css/index.css'
        context['js_file']              = 'inc/js/index.js'
        return context


# Intro (회사소개)
class IntroView(ListView):

    template_name                       = 'subpage/intro.html'
    context_object_name                 = 'data'

    def get_queryset(self):
        return ''

    def get_context_data(self, **kwargs):
        context                         = super().get_context_data(**kwargs)
        return context
        