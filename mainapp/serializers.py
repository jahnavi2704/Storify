from .models import *
from rest_framework import serializers

class genreserializer(serializers.ModelSerializer):
	class Meta:
		model=articles
		fields=('article' , 'title' , 'authorId')

