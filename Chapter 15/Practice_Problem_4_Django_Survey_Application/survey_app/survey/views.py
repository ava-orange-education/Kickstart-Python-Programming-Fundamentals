from django.shortcuts import render, redirect, get_object_or_404
from .models import Survey, Question, Choice
from .forms import SurveyResponseForm

def survey_list(request):
    surveys = Survey.objects.all()
    return render(request, 'survey/survey_list.html', {'surveys': surveys})

def survey_detail(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.question_set.all()
    if request.method == 'POST':
        for question in questions:
            choice_id = request.POST.get(str(question.id))
            if choice_id:
                choice = Choice.objects.get(id=choice_id)
                choice.votes += 1
                choice.save()
        return redirect('survey_results', survey_id=survey.id)
    return render(request, 'survey/survey_detail.html', {'survey': survey, 'questions': questions})

def survey_results(request, survey_id):
    survey = get_object_or_404(Survey, id=survey_id)
    questions = survey.question_set.all()
    return render(request, 'survey/survey_results.html', {'survey': survey, 'questions': questions})
