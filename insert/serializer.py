from rest_framework import serializers, status
from django.contrib.auth.models import User
from .models import UnivStudent

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class StudentSerializer(serializers.ModelSerializer):
    """
    A student serializer to return the student details
    """
    user = UserSerializer(required=True)

    class Meta:
        model = UnivStudent
        fields = ('user', 'subject_major',)

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of student
        :return: returns a successfully created student record
        """
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student, created = UnivStudent.objects.update_or_create(user=user,
                            subject_major=validated_data.pop('subject_major'))
        return student