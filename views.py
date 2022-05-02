

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect

from . import models
# Create your views here.
def index(request):
    print("Do I come here")
    if request.method == 'POST':
        print("Do I come here in f")

        dt = models.PollForm(request.POST)
        
        if dt.is_valid():
          
            print("Do I come here in fffff")  
        
            #choiceText = dt['choice_text'].value()
            #print("CHoice TExt")
            chc = models.PollModel.objects.get(choice_text=dt['choice_text'].value())
            chc.votes += 1
            chc.save()
            return HttpResponseRedirect('/1/results')
        
    return render(request, 'index.html', { 'question': models.QuestionModel.objects.first()})

def results(request):
    poll_data = models.PollModel.objects.all()
    return render(request, 'index1.html', { 'poll_data': poll_data })