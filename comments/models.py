from django.db import models
import ipdb
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    user_comments = models.ForeignKey('users.User',on_delete=models.CASCADE,related_name="Comments")
    weapon = models.ForeignKey(
        'weapons.Weapon',
        on_delete=models.CASCADE,
        related_name="Comments"
    )
    commented_at= models.DateTimeField(auto_now_add=True)
    