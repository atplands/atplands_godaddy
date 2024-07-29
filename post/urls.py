from django.urls import path
from post.views import index, login_index, NewPost, PostDetail, Tags, like, favourite

urlpatterns = [
    path('', index, name='landbook_index'),
    path('user', login_index, name='lb_login_index'),
    path('newpost', NewPost, name='newpost'),
    path('<uuid:post_id>', PostDetail, name='post-details'),
    path('tag/<slug:tag_slug>', Tags, name='tags'),
    path('<uuid:post_id>/like', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),

]
