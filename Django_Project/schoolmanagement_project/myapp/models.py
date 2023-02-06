from django.db import models

# Create your models here.
class Feedback(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.CharField(max_length=100)
	feedback=models.TextField()

	def __str__(self):
		return self.name

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.CharField(max_length=100)
	gender=models.CharField(max_length=100)
	dob=models.CharField(max_length=100)
	aadhaar=models.CharField(max_length=100)
	state=models.CharField(max_length=100)
	city=models.CharField(max_length=100)
	pincode=models.CharField(max_length=100)
	address=models.TextField()
	password=models.CharField(max_length=100)
	photo=models.ImageField(upload_to="photo/",default="")

	def __str__(self):
		return self.fname +" - "+ self.lname