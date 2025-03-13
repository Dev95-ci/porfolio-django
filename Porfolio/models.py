from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    
    
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='projects/images/')
    caption = models.CharField(max_length=200, blank=True, null=True)  # Optionnel, pour une légende

    def __str__(self):
        return f"Image pour {self.project.title}"
