## 2022-05-31 서브페이지를 위한 경로 추가 (Index)
## 2022-06-01 게시판 및 에디터 추가
from django.contrib import admin
from django.urls import path, include
from layout import views

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', views.MainView.as_view()),
    path('intro/', views.IntroView.as_view()),
    path('board/', include('board.urls'))
]

# Summernote 설정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += [path('summernote/', include('django_summernote.urls'))]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)