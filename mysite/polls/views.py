from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice, Chart
from django.template import loader
from django.urls import reverse
from django.views import generic
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
    expenses_value = [30000, 0]
    cash_flow_value = [35000, 0]
    passive_income_value = [0, 25000]
    cash_on_hand_labels = ["Fixed Deposit", "Liquid Assets"]
    cash_on_hand_values = [25000, 75000]
    your_capital_labels = ["Unit Trust", "House", "Shares", "Insurance", "Shares"]	
    your_capital_values = [32, 60, 12, 23, 14]

    expenses_value = map(json.dumps, expenses_value)
    cash_flow_value = map(json.dumps, cash_flow_value)
    passive_income_value = map(json.dumps, passive_income_value)
    cash_on_hand_labels = map(json.dumps, cash_on_hand_labels)
    cash_on_hand_values = map(json.dumps, cash_on_hand_values)
    your_capital_labels = map(json.dumps, your_capital_labels)
    your_capital_values = map(json.dumps, your_capital_values)
    

    context = {
        'expenses_value': expenses_value,
        'cash_flow_value': cash_flow_value,
        'passive_income_value': passive_income_value,
        'cash_on_hand_labels': cash_on_hand_labels,
        'cash_on_hand_values': cash_on_hand_values,
        'your_capital_labels': your_capital_labels,
        'your_capital_values': your_capital_values,
        
    }
    return render(request, 'polls/charts.html', context)