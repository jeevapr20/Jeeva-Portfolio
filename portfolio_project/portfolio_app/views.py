from django.shortcuts import get_object_or_404, render
from .forms import ContactForm
from portfolio_app.models import Project
from .models import Project, ContactMessage
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages



def index(request):
    # Fetch all projects to display on the page
    projects = Project.objects.all()

    if request.method == 'POST':
        # Process the contact form submission
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the ContactMessage model
            ContactMessage.objects.create(**form.cleaned_data)
            
            # Add a success message
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to avoid duplicate form submission on refresh
            return HttpResponseRedirect(reverse('home'))
        else:
            # Add an error message if the form is invalid
            messages.error(request, "Please fill out all fields correctly.")
    else:
        # Initialize an empty form for GET requests
        form = ContactForm()

    # Render the template with the necessary context
    return render(request, 'portfolio_app/index.html', {
        'projects': projects,
        'form': form,
    })
    
def contact(request):
    return render(request,'portfolio_app/contact.html')

def about(request):
    return render(request,'portfolio_app/about.html')

def hero(request):
    return render(request,'portfolio_app/hero.html')

def portfolio(request):
    projects=Project.objects.all()
    context={
        "projects":projects
    }
    return render(request,'portfolio_app/portfolio.html',context)

def portfolio_details(request,pk):
    project = get_object_or_404(Project, pk=pk)
    context = {
        "project": project
    }
    return render(request,'portfolio_app/portfolio-details.html',context)

def resume(request):
    return render(request,'portfolio_app/resume.html')

def skills(request):
    return render(request,'portfolio_app/skills.html')

