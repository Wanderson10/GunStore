from rest_framework import serializers
from .models import Atributes


class AtributeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Atributes
       fields = ["id","caliber","system","capacity","weight","length","material","model","operation", "finishing"]
       read_only_fields =["id"]
    
    