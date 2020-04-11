from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	roll = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100,blank=True)
	department = models.CharField(max_length=100)
	phone = models.CharField(max_length=10,blank=True)
	email = models.CharField(max_length=100,blank=True)
	course = models.CharField(max_length=100,blank=True)
	fatherName = models.CharField(max_length=100,blank=True)
	address = models.CharField(max_length=1000,blank=True)
	password = models.CharField(max_length=100,blank=True)
	gender = models.CharField(max_length=10,blank=True)
	bloodGroup = models.CharField(max_length=3,blank=True)
	fcmtoken = models.CharField(max_length=500, blank=True)
	dob = models.CharField(max_length=15,blank=True)
	yearOfAdmission = models.IntegerField(blank = True, default = 2018)
	reg_time = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name 


class Complain(models.Model):
	complainby = models.ForeignKey(Student, on_delete=models.CASCADE,null=True,editable=False)
	complain = models.TextField()
	complainheader=models.TextField(null=True)
	complaintype=models.TextField(null=True)
	complainsubtype=models.TextField(blank=True, null=True)
	def __str__(self):
		if self.complainby:
			return "complain by " + self.complainby.name 
		return "complain by anonymous"

class CouncilandCell(models.Model):
	name = models.CharField(max_length=100, blank=False)
	image = models.ImageField(null=True,blank=False)
	def __str__(self):
		return self.name

class Club(models.Model):
	councilname = models.ForeignKey(CouncilandCell, on_delete = models.CASCADE)
	name = models.CharField(max_length=100, blank=True)
	clubimage = models.ImageField(null=True,blank=True)
	def __str__(self):
		return self.name

class Notification(models.Model):
	# coun/cilname = models.ForeignKey(CouncilandCell, on_delete = models.CASCADE)
	clubname = models.ForeignKey(Club, on_delete = models.CASCADE,verbose_name='Club/Cell Name',blank=False,null =True)
	LOCATIONS =  [(i.strip(),i.strip()) for i in open('listPlaces.txt','r').readlines() if i.strip() != '']

	# clubname = ChainedForeignKey(Club, chained_field="councilname",chained_model_field="councilname",
 #        auto_choose=True,
 #        show_all=False,
 #        sort=True, null=True,blank=True)
	notification = models.CharField(max_length= 1000, verbose_name='Title')
	notification_header = models.CharField(max_length = 100,verbose_name='Description')
	notification_pic = models.ImageField(null=True,blank=True,verbose_name='Image')
	datetime = models.DateTimeField()
	location = models.CharField(max_length = 300)
	map_location = models.CharField(max_length = 300,choices = LOCATIONS, null=True,blank=True)
	viewedby = models.ManyToManyField(Student,editable=False,related_name='viewedby')
	interested = models.ManyToManyField(Student,editable=False,related_name='interested')
	
	class Meta:
		ordering = ['-datetime']

	def __str__(self):
		return self.notification_header

class ImpContact(models.Model):
	name = models.CharField(max_length=100,blank=True)
	email = models.CharField(max_length=100,blank=True)
	phone = models.CharField(max_length=10,blank=True)
	role_type = models.CharField(max_length=20,blank=True)
	
	def __str__(self):
		return self.name

class TimeTable(models.Model):
	department = models.CharField(max_length=100,blank=True)
	year = models.IntegerField(blank = True, default = 1)
	tableimage = models.ImageField(null=True,blank=True)
	
	def __str__(self):
		return self.department
	
class Exam(models.Model):
	subject_code = models.CharField(max_length=10,blank=True)
	date_and_time = models.DateTimeField(auto_now_add=False)
	date_and_time.editable = True
	location = models.CharField(max_length=20,blank=True)
	
	def __str__(self):
		return self.subject_code

	
	
	
