from App_post import views
from django.urls import path

app_name = "App_post"

urlpatterns = [
    path('post_list/', views.PostList.as_view()),
    path('create_post/', views.CreatePost.as_view()),
    path('post_detail/<id>', views.PostDetail.as_view()),
    path('post_update/<id>', views.PostUpdate.as_view()),
    path('post_delete/<id>', views.PostDelete.as_view()),
    path('<int:pk>/like/', views.LikeApi.as_view()),
    path('<int:pk>/LikedUserList/', views.LikedUserList.as_view()),
    path('<int:post_id>/Create_comment/', views.Create_comment.as_view()),
    path('<int:pk>/get_comment/', views.CommentList.as_view()),
    path('<int:pk>/update_comment/', views.update_comment.as_view()),
    path('<int:pk>/delete_comment/', views.delete_comment.as_view()),
    

    
    path('task_list/', views.TaskList.as_view()),
    path('task_create/', views.TaskCreate.as_view()),
    path('task_detail/<id>', views.TaskDetail.as_view()),
    path('task_update/<id>', views.TaskUpdate.as_view()),
    path('task_delete/<id>', views.TaskDelete.as_view()),
 ]