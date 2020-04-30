from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User


# Create your models here.
GENDER_choices = (
	('male','MALE'),
	('female','FEMALE'),
	('other','OTHER'),
)

class userInfo(models.Model):
	#userId = models.CharField(primary_key = True, max_length = 25, unique=True)
	name = models.CharField(max_length=50)
	user = models.OneToOneField(User, primary_key=True, related_name='profile', on_delete=models.CASCADE)
	dateofbirth = models.DateField()
	emailId = models.EmailField(max_length = 75)
	profession = models.TextField()
	gender = models.CharField(max_length=50,choices = GENDER_choices, default = 'female')
	phonenumber = models.CharField(max_length = 10)
	
	def __str__(self):
		return  str(self.user)


GENRE_choices = (
	('education','EDUCATION'),
	('horror','HORROR'),
	('thriller','THRILLER'),
	('comedy','COMEDY'),
	('action','ACTION'),
	('romance','ROMANCE'),
)

class genre(models.Model):
	genreId = models.AutoField(primary_key = True)
	genre = models.CharField(max_length=50,choices = GENRE_choices, default = 'education')

	def __str__(self):
		return str(self.genre)

# class subscription(models.Model):
# 	userId = models.CharField(primary_key = True,max_length = 25, unique=True)
# 	subscription_date = models.DateTimeField(default = timezone.now)

# 	def __str__(self):
# 		return str(self.userId)

class subscription(models.Model):
	userId = models.ForeignKey(userInfo, on_delete = models.CASCADE)
	subscription_date = models.DateTimeField(default = timezone.now)

	def __str__(self):
		return str(self.userId)

class articles(models.Model): 
	articleId = models.AutoField(primary_key = True)
	genre = models.ManyToManyField(genre)
	authorId = models.ForeignKey(userInfo, on_delete = models.CASCADE)
	dateposted = models.DateTimeField(default = timezone.now)
	article = models.TextField()
	title = models.CharField(max_length = 50)
	posted = models.BooleanField(default = False)
	views= models.IntegerField()
	upvotes = models.IntegerField()
	downvotes = models.IntegerField()

	def __str__(self):
		return str(self.title)



class comments(models.Model):
	commentId = models.AutoField(primary_key = True)
	articleId = models.ForeignKey(articles,on_delete=models.CASCADE)
	comment_data = models.TextField()
	upvotes = models.IntegerField(blank=True)
	downvotes = models.IntegerField(blank=True)
	userId = models.ForeignKey(userInfo, on_delete = models.CASCADE)
	datecommented = models.DateTimeField(default = timezone.now)
                                                                                                   
	def __str__(self):
		return str(self.commentId)

class favauthors(models.Model):
	userId =  models.ForeignKey(userInfo,on_delete=models.CASCADE)
	authorId =  models.ManyToManyField(articles)

	def __str__(self):
		return str(self.userId)

class favgenres(models.Model):
	userId =  models.ForeignKey(userInfo,on_delete=models.CASCADE)
	genre =  models.ManyToManyField(genre)

	def __str__(self):
		return str(self.userId)

###################################

'''class Userprofile(models.Model):
	user  = models.OneToOneField(User,on_delete=models.CASCADE, primary_key = True)
	name = models.CharField(max_length=50)
	dateofbirth = models.DateField()
	profession = models.CharField(max_length=500)
	gender = models.CharField(max_length=50,choices = GENDER_choices, default = 'female')
	phonenumber = models.CharField(max_length = 10)

	def __str__(self):
		return self.user.username'''