from django.db import models
from django.contrib.auth.models import User


class UnivStudent(models.Model):
    """
    A class based model for storing the records of a university student
    Note: A OneToOne relation is established for each student with User model.
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,)
    subject_major = models.CharField(name="subject_major", max_length=60)