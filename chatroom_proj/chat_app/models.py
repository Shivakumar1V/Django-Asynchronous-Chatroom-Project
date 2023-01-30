from django.db import models

# Create your models here.

class Chatroom(models.Model):
    name = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.name

class Chat(models.Model):
    chat_content = models.CharField(max_length=5000)
    user = models.CharField(max_length=5000)
    room = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    timestamp = models.DateField(auto_now_add=True)