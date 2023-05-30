from rest_framework import serializers
from .models import User
from comments.serializers import CommentsSerializer
from comments.models import Comment
import ipdb
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ["id","username","email","date_joined","phone_number","cpf","password","is_superuser"]
        extra_kwargs ={'password' : {'write_only':True}}
    def get_user_comments(self, obj:User):
        return obj.user.Comments
    def create(self, validated_data: dict) -> User:
        print(validated_data)
        
            
        return User.objects.create_user(**validated_data)
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.username
        # ...

        return token



       