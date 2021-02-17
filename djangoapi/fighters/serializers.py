from rest_framework import serializers
from fighters.models import Fighter

# we want to send Fighter model over http

class FighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fighter
        fields = "__all__"
        #fields = ["id", "name", ...] proper way

    #modify incoming data
    def create(self, validated_date): #validated is a dictionary
      validated_date["description"] = validated_date
      return super().create(validated_date)