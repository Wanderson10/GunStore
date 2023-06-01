from rest_framework import serializers
from .models import Comment
from users.models import User

class CommentsSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
     model = Comment
     fields = ["id","comment", "user_comments","commented_at","weapon","user_name"]
     read_only_fields = ["id","user_comments", "commented_at"]

    

     
    def get_user_name(self, obj:Comment):
        return  obj.user_comments.username