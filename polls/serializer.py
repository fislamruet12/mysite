from .models import Question

from rest_framework import serializers, status

class Questionserializer(serializers.ModelSerializer):
   class Meta:
       model=Question
       fields= ('question_text','pub_date')

