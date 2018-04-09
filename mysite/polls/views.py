from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.urls import reverse
from .models import Question, Choice
import json


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

#View of the charts

def charts(request):
    question = Question.objects.all()
    choice = Choice.objects.all()

    if request.method == 'POST':
        selected_choice = Choice.objects.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()

    questions = list(Question.objects.values_list('question_text'))
    choices = list(Choice.objects.values_list('choice_text'))
    votes = list(Choice.objects.values_list('votes'))
    question1_total_votes = list(Choice.objects.values_list('votes').filter(question_id=1))
    question2_total_votes = list(Choice.objects.values_list('votes').filter(question_id=2))
    
    question1_choice1_label = choices[0]
    question1_choice2_label = choices[1]
    question2_choice1_label = choices[2]
    question2_choice2_label = choices[3]

    question1_choice1 = list(question1_total_votes[0])
    question1_choice2 = list(question1_total_votes[1])
    question2_choice1 = [0] + list(question2_total_votes[0])
    question2_choice2 = [0] + list(question2_total_votes[1])

    # Calculate the sum of votes for question 1 and 2.
    l = []
    counter1 = 0
    for x in question1_total_votes:
        l = l + list(question1_total_votes[counter1])
        counter1 = counter1 + 1
    
    k = []
    counter2 = 0
    for x in question2_total_votes:
        k = k + list(question2_total_votes[counter2])
        counter2 = counter2 + 1

    choices_chosen = [sum(l), sum(k)]

    questions = map(json.dumps, questions)
    choices = map(json.dumps, choices)
    votes = map(json.dumps, votes)
    choices_chosen = map(json.dumps, choices_chosen)
    question1_choice1_label = map(json.dumps, question1_choice1_label)
    question1_choice2_label = map(json.dumps, question1_choice2_label)
    question2_choice1_label = map(json.dumps, question2_choice1_label)
    question2_choice2_label = map(json.dumps, question2_choice2_label)
    question1_choice1 = map(json.dumps, question1_choice1)
    question1_choice2 = map(json.dumps, question1_choice2)
    question2_choice1 = map(json.dumps, question2_choice1)
    question2_choice2 = map(json.dumps, question2_choice2)

    context = {
        'question': question,
        'choice': choice,
        'questions': questions,
        'choices': choices,
        'votes': votes,
        'choices_chosen': choices_chosen,
        'question1_choice1_label': question1_choice1_label,
        'question1_choice2_label': question1_choice2_label,
        'question2_choice1_label': question2_choice1_label,
        'question2_choice2_label': question2_choice2_label,
        'question1_choice1': question1_choice1,
        'question1_choice2': question1_choice2,
        'question2_choice1': question2_choice1,
        'question2_choice2': question2_choice2,
    }
    return render(request, 'polls/charts.html', context)