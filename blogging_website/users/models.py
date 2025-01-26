from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100) # i have created a model for the user
    email = models.EmailField(max_length=100) # the user will have a name, email, password, created_at and updated_at
    password = models.CharField(max_length=100) # the name will be a character field with a max length of 100
    created_at = models.DateTimeField(auto_now_add=True) # the email will be an email field with a max length of 100
    updated_at = models.DateTimeField(auto_now=True) # the password will be a character field with a max length of 100

    def __str__(self): # i have used the dunder str method to return the name of the user
        return self.name # this will return the name of the user

# Extra Functionality Added:
# This functionality i have added is extra and is not required for the project, but if in future you want to add a user model then can be utilized.  
 # i have created this model to be used for the user
 # the user will have a name, email, password, created_at and updated_at
 # the name will be a character field with a max length of 100
 # the email will be an email field with a max length of 100
 # the password will be a character field with a max length of 100
 # the created_at will be a date time field that will be automatically added when the user is created
 # the updated_at will be a date time field that will be automatically updated when the user is updated
 # the __str__ method will return the name of the user
 