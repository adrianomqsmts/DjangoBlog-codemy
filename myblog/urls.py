from django.urls import path
# from . import views
from .views import HomeListView, ArticleDetailView, AddPostCreateView, PostUpdateView, PostDeleteView, CategoryCreateView, CategoryListView, LikeView, CommentCreateView

urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeListView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('add_post/', AddPostCreateView.as_view(), name='add_post'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('article/edit/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', PostDeleteView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryListView.as_view(), name='category'),
    path('like/<int:pk>/', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='add_comment'),

]
