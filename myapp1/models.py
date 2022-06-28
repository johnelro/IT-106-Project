from django.db import models

class MysimpleModel(models.Model):
	col = models.CharField(max_length=15)

