from django import forms
from .models import Choice

class SurveyResponseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(SurveyResponseForm, self).__init__(*args, **kwargs)
        for question in questions:
            choices = question.choice_set.all()
            self.fields[str(question.id)] = forms.ChoiceField(
                label=question.question_text,
                choices=[(choice.id, choice.choice_text) for choice in choices],
                widget=forms.RadioSelect,
                required=True
            )
