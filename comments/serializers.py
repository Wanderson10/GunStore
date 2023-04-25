from rest_framework import serializers
from .models import Comment
from users.models import User
import ipdb
class CommentsSerializer(serializers.ModelSerializer):
  
    class Meta:
     model = Comment
     fields = ["id","comment", "user_comments","commented_at"]
     read_only_fields = ["id","user_comments", "commented_at"]

     
