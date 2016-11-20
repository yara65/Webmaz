from django.shortcuts import render

# Create your views here.

from .models import Post 
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views.generic import ListView, DetailView

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/index.html', {'question': question})

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def contact(request):
    return render_to_response('contact.html')
    
class PostsListView(ListView): 
    model = Post                  

class PostDetailView(DetailView):
    model = Post
    
#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index
       
