from django.shortcuts import render
# from django.http import HttpResponse
from .models import Track
# from .forms import SubscriberForm

def index(request):
    tracks = Track.objects.filter(is_active=True)
    return render(request, 'shop/index.html', locals())

def about(request):
    return render(request, 'shop/about.html', locals())


# def detail(request, question_id):
#     return HttpResponse("You're looking %s at question." % question_id)
#
# def results(request, question_id):
#     response = "You're looking at %s the results of question ."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
