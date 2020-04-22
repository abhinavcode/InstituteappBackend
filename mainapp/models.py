from django.db import models
from django.contrib.auth.models import User
import requests as req
import json
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

class POR(models.Model):
	name = models.CharField(max_length=100, blank=False,default="")
	email = models.CharField(max_length=100, blank=False,default="")
	phone = models.CharField(max_length=100, blank=False,default="")
	councilname = models.CharField(max_length=100, blank=False,default="")
	postion = models.CharField(max_length=100, blank=False,default="")
	image = models.ImageField(null=True,blank=False)
	dept = models.CharField(max_length=100, blank=False,default="")
	responsibility = models.CharField(max_length=100, blank=False,default="")
	def __str__(self):
		return self.name


class Club(models.Model):
	councilname = models.ForeignKey(CouncilandCell, on_delete = models.CASCADE)
	name = models.CharField(max_length=100, blank=False)
	clubimage = models.ImageField(null=True,blank=False)
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
	notification = models.CharField(max_length= 10000, verbose_name='Description')
	notification_header = models.CharField(max_length = 100,verbose_name='Title')
	notification_pic = models.ImageField(null=True,blank=True,verbose_name='Image')
	datetime = models.DateTimeField(null=False, blank=False)
	datetime.editable = True
	location = models.CharField(max_length = 300)
	map_location = models.CharField(max_length = 300,choices = LOCATIONS, null=True,blank=True)
	viewedby = models.ManyToManyField(Student,editable=False,related_name='viewedby')
	interested = models.ManyToManyField(Student,editable=False,related_name='interested')

	def save(self, *args, **kwargs):
		jsondata = {"notification": {"title": self.notification_header,"body" : self.notification,"location":self.location,"year":self.datetime.year,"month":self.datetime.month,"hour":self.datetime.hour,"minutes":self.datetime.minute},"to": "/topics/"+ self.clubname.name.split()[0]}
		firebase_messaging_req =req.post(url="https://fcm.googleapis.com/fcm/send",data=json.dumps(jsondata),headers = {"Content-Type":"application/json","Authorization":"key=AAAAIJ0yPMw:APA91bFSHkaDO3-s5c6K3U8H0LQFrU7PUz1GIMlaW5lit6dtsh46JUgvJD_cT0l79P_pJQRfeoqs57WjG9DqMdVFpglDjBl9CnZ_lINpmo7AQxol6p7U0BdpPEbh5M2PTpiCiZdx7vOP"})
		print(firebase_messaging_req.text)
		super(Notification, self).save(*args, **kwargs)

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
