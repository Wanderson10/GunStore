from django.shortcuts import render
from .models import Comment
from .serializers import CommentsSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly




class CommentView(generics.ListCreateAPIView):
     
     authentication_classes=[JWTAuthentication]
     permission_classes =[IsAuthenticatedOrReadOnly]
     serializer_class = CommentsSerializer
     queryset = Comment.objects.all()
    
     def perform_create(self, serializer):
        serializer.save(  user_comments = self.request.user)
        
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[JWTAuthentication]
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = CommentsSerializer
  
    queryset = Comment.objects.all()
    
    lookup_url_kwarg = 'comment_id'