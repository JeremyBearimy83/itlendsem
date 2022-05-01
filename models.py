from django.db import models
from django import forms

# Create your models here.
class BlogModel(models.Model):
    name = models.CharField(max_length = 150)



class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        exclude = ('likes',)

