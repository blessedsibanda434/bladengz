from django.urls import path, re_path
from .views import PostListView, PostDetailView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    #re_path('^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',PostDetailView.as_view(), name='post-detail'),
    path('<int:year>/<int:month>/<int:day>/<slug>/', PostDetailView.as_view(), name='post_detail'),
]