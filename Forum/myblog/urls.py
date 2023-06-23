
from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('article/<int:pk>',views.ArticleDetail.as_view(),name="article_detail"),
    path('add_post/',views.AddPostView.as_view(),name="add_post"),
    path('add_category/',views.AddCategoryView.as_view(),name="add_category"),
    path('article/edit/<int:pk>',views.EditPost.as_view(),name="update_post"),
    path('article/<int:pk>/delete',views.DeletePost.as_view(),name="delete_post"),
    path('category/<str:cats>/',views.CategoryView,name="categorys"),
    path('category_list/',views.CategoryListView,name="categorys_list"),
    path('like/<int:pk>/',views.LikeView,name="like_post"),
    path('article/<int:pk>/add_comment/',views.AddCommentView.as_view(),name="add_comment"),
]
