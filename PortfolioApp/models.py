from django.db import models

class UserPortfolioInfo(models.Model):
    '''
        This Model Class will contain the information of user.
    '''
    Firstname = models.CharField(max_length=50, blank=False)
    Lastname = models.CharField(max_length=50, blank=False)
    College_name = models.CharField(max_length=50, blank=False)
    Email = models.EmailField(max_length=254)
    Phone_number = models.CharField(blank=True, max_length=10)
    GitHublink = models.URLField(max_length=500)
    Linkedin = models.URLField(max_length=500)
    Instagram = models.URLField(max_length=500)
    project1 = models.TextField()
    project2 = models.TextField(blank=True)
    project3 = models.TextField(blank=True)
    project4 = models.TextField(blank=True)
    Hobbies = models.TextField()

    def __str__(self):
        return f"{self.Firstname} + {self.Lastname}"
    
