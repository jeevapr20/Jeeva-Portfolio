from django.shortcuts import get_object_or_404, render

from portfolio_app.models import Project

def index(request):
    projects = Project.objects.all()
    for project in projects:
        print(project.pk, project.title)  # Debugging line
    return render(request, 'portfolio_app/index.html', {'projects': projects})

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

