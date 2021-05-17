from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'blog'

#modelViewSetのurl設定
router = DefaultRouter()
router.register('blog', views.BlogViewSet)

#genericsの汎用viewで作成したviewのurl設定
urlpatterns = [
    path('',include(router.urls)),
]