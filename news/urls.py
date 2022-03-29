
from unicodedata import name
from django.urls import re_path
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.news_today,name = 'newsToday'),
    re_path('^today/$',views.news_today,name='newsToday'),
    re_path('^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name='pastNews'),
    re_path('^article/(\d+)',views.article,name='article'),
    re_path('^search/',views.search_results,name='search_results'),
    re_path('^new/article$',views.new_article,name='new-article')


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)