from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import  reverse 
from django.views import generic

from . models import Question, Choice
# Create your views here.

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')
#     context = { 'latest_question_list' : latest_question_list}
#     return render(request, 'votes/index.html', context)


class IndexView(generic.ListView):
    template_name = 'votes/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Question
    template_name = 'votes/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'votes/results.html'


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'votes/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('votes:results', args=(question.id,)))
