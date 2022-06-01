from django import forms
from .models import Board
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class BoardWrite(forms.ModelForm):
    title                                   = forms.CharField(
        label                               = '제목',
        widget                              = forms.TextInput(
            attrs                           = {
                'placeholder'               : '제목'
            }
        ),
        required                            = True
    )
    content                                 = SummernoteTextField()
    options                                 = (
        ('notice', '공지사항')
    )
    board_name                              = forms.ChoiceField(
        label                               = '게시판',
        widget                              = forms.Select(),
        choices                             = options
    )
    field_order                             = [
        'title',
        'board_name',
        'content'
    ]

    class Meta:
        model                               = Board
        fields                              = [
            'title',
            'content',
            'board_name'
        ]
        widgets                             = {
            'content'                       : SummernoteWidget()
        }

    def clean(self):
        cleaned_data                        = super().clean()

        title                               = cleaned_data.get('title', '')
        content                             = cleaned_data.get('content', '')
        board_name                          = cleaned_data.get('board_name', 'notice')

        if(title == ''):
            self.add_error('title', '제목을 입력하세요!')
        elif(content == ''):
            self.add_error('title', '내용을 입력하세요!')
        else:
            self.title                      = title
            self.content                    = content
            self.board_name                 = board_name