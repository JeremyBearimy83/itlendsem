from django.db import models
from django import forms

# Create your models here.

# Create your models here.
class QuestionModel(models.Model):
    question = models.CharField(max_length=500, primary_key=True)
    date_published = models.DateTimeField()

class PollModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100, choices = (('EASY', 'EASY'), ('DIFFICULT', 'DIFFICULT')))
    votes = models.IntegerField()



class PollDiffForm(forms.Form):
    choice = forms.ChoiceField(choices = (('EASY', 'EASY'), ('DIFFICULT', 'DIFFICULT')))

#class PollForm(forms.ModelForm):
 #   class Meta:
  #      model = PollModel
   #     exclude = ('votes', 'question')