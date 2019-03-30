from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$',views.index, name='index'),

    # /music/ID/
    path('<int:album_id>', views.detail, name='detail'),

    # /music/ID/favorite
    path('<int:album_id>/favorite', views.favorite, name='favorite'),

]

