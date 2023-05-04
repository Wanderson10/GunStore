from django.db import models
class GroupWeapons(models.TextChoices):
    Pistol = 'Pistol'
    KNIFE = 'Knife'
    BOW = 'Bow'
    CROSSBOW = 'CrossBow'
    Revolver ='Revolver'
    UNINFORMED = 'Uniformed'
class Weapon(models.Model):
    name = models.CharField(max_length=100)
    tipe = models.CharField(  max_length=10,
        choices = GroupWeapons.choices,
        default= GroupWeapons.UNINFORMED)
    price = models.IntegerField()
    descripition = models.TextField(max_length=1000)
    image = models.CharField(max_length=200)
    image2 = models.CharField(max_length=200)
    image3 =models.CharField(max_length=200,blank=True)
    atributes = models.ForeignKey(
        "atributes.Atributes",
        on_delete=models.CASCADE,
        related_name="weapons",
    )