from django.contrib import admin
from .models import QuestionModel, PollModel

admin.site.register(QuestionModel)
admin.site.register(PollModel)

# Register your models here.
