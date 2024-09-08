from django.shortcuts import render
from .forms import ContactForm

def home(request):
    context = {'title': 'Hello, Django!'}
    return render(request, 'myapp/home.html', context)

def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            submitted = True
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form, 'submitted': submitted})

