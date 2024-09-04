from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    employeeId = models.CharField(max_length=50, unique=True)
    employeeName = models.CharField(max_length=100)
    employeeDepartment = models.CharField(max_length=100)
    employeeDesignation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Only in Employee model
    password = models.CharField(max_length=255)  # Only in Employee model
    def __str__(self):
        return self.employeeName
    

class Card(models.Model):
    cardName = models.CharField(max_length=255)
    columnId = models.CharField(max_length=50)  # Assuming columnId is a string for simplicity
    def __str__(self):
        return self.cardName
    

class Comment(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text
    
    
class Board(models.Model):
    employeeId = models.CharField(max_length=50)
    employeeName = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=7)

