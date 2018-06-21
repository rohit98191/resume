from .models import Required
from rest_framework import serializers

class RequiredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Required
        fields= ("id",'name','email_id','phone_no',"be_cgpa","hsc_percent","ssc_percent")



