from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView
from .models import Project, ProjectImage
from django.contrib import messages
from django.shortcuts import render, get_object_or_404




def index(request):
    return render(request, 'porfolio/home.html')


def about(request):
    return render(request, 'porfolio/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['nom']
        email = request.POST['mail']
        message = request.POST['content']
        
        if name and email and message is not None:
            # Envoi de l'email
            envoi = send_mail(
                f'Nouveau message de {name} via le portfolio',
                message,
                email,
                ['st4074677@gmail.com'],
            )
            
            if envoi:
                # Ajouter un message de succès
                messages.success(request, 'Votre message a été envoyé avec succès ! Je reviendrai vers vous bientôt.')
                return redirect('contact')
        else:
            messages.success(request, "Veuillez remplir tous les champs s'il vous plaît")
        
        
        
    return render(request, 'porfolio/contact.html')


class ProjectListView(ListView):
    model = Project
    template_name = 'porfolio/project_list.html'
    context_object_name = 'projects'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'porfolio/project_detail.html'
    context_object_name = 'project'



def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    images = project.images.all()  # Grâce à related_name="images"
    return render(request, 'porfolio/project_detail.html', {'project': project, 'images': images})


