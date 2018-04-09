from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .forms import SubscriberForm

def index(request):
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()
    return render(request, 'shop/index.html', locals())

def detail(request, question_id):
    return HttpResponse("You're looking %s at question." % question_id)

def results(request, question_id):
    response = "You're looking at %s the results of question ."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)