from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            submitted = True
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'submitted': submitted})
