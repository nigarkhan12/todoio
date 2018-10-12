from django.contrib.auth.models import User
from django.db import models
import datetime
from uuid import uuid4


class TodoItem(models.Model):
	uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	title_text=models.CharField(max_length=200)
	reminder = models.DateTimeField(null=True)
	notes = models.TextField(null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)