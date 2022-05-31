## 2022-05-31 서브페이지를 위한 경로 추가 (Index)


from django.contrib import admin
from django.urls import path
from layout import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view()),
    path('intro/', views.IntroView.as_view())
]
