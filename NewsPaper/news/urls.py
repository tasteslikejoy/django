from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

app_name = 'appointment_form'

urlpatterns = [
    path('', NewsPost.as_view(), name='post_list'),
    path('<int:pk>', cache_page(10)(NewsDetail.as_view()), name='news_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('post/create/', PostCreate.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('appointment/', AppointmentView.as_view(), name='appointment_form'),
    path('categories/', CategoryList.as_view(), name='category_list'),
    path('inc/', NewsPostRandom.as_view(), name='random'),
    path('categorydetail/<int:pk>', CategoryDetail.as_view(), name='categorydetail'),
    path('categorydetail/<int:pk>/subscribe/', add_subscribers, name='subscribe'),
]