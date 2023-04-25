from rest_framework import serializers
from .models import Weapon
from atributes.serializer import AtributeSerializer
from atributes.models import Atributes






class WeaponSerializer(serializers.ModelSerializer):
    atributes = AtributeSerializer()
    class Meta:
       
        model = Weapon
        
        fields = "__all__"
   
    def create(self, validated_data):

        atributes_dict = validated_data.pop("atributes")
        
        atribute, _ = Atributes.objects.get_or_create(**atributes_dict)

        wapon_obj = Weapon.objects.create(**validated_data, atributes=atribute)

        return wapon_obj
    def update(self, instance: Weapon, validated_data: dict):
        atributes_data: dict = validated_data.pop('atributes', None)

        if atributes_data:
            atributes, _ = Atributes.objects.get_or_create(**atributes_data)

            instance.atributes = atributes
            
        for key, value in validated_data.items():
             setattr(instance, key, value)
        instance.save()

        return instance
    