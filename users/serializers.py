from rest_framework import serializers
from .models import User
from comments.serializers import CommentsSerializer
from comments.models import Comment
import ipdb
class UserSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = User
        fields = ["id","username","email","date_joined","phone_number","cpf","is_employee","password"]
        extra_kwargs ={'password' : {'write_only':True}}
    def get_user_comments(self, obj:User):
        return obj.user.Comments

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
           

            return User.objects.create_superuser(**validated_data)


        else:
            
            return User.objects.create_user(**validated_data)
   
    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance





       