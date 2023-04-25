from django.urls import path
from . import views


urlpatterns = [
    path("comments/", views.CommentView.as_view()),
     path("comments/<int:comment_id>",views.CommentDetailView.as_view()),
]