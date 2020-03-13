from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mood(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	emoji = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f"{self.title} | {self.emoji}"

class Action(models.Model):
	title = models.CharField(max_length=100, null=True, blank=True)
	emoji = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f"{self.title} | {self.emoji}"

class MoodLog(models.Model):
	mood = models.ForeignKey(Mood, on_delete=models.CASCADE, null=True, blank=True)
	action = models.ForeignKey(Action, on_delete=models.CASCADE, null=True, blank=True)
	note = models.TextField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f"{self.mood.title}"