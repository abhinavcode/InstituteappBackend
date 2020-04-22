#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files import File
import json
import requests as req
from base64 import *
from django.utils import timezone
import string
import random
import datetime

def randomString(stringLength=10):
    """Generate a random string of fixed length """

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@csrf_exempt
def checkregister(request):

    response = {}
    response['status'] = 0

    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        email = post['email']
        try:
            user = User.objects.get(email__iexact=email)
            if not user.check_password(post['password']):
                    raise Exception
            student= Student.objects.get(user=user)
            response['name'] = student.name
            response['roll'] = student.roll
            response['phone'] = student.phone
            response['department'] = student.department
            response['yearOfAdmission'] = student.yearOfAdmission
            response['course'] = student.course
            response['fatherName'] = student.fatherName
            response['address'] = student.address
            response['gender'] = student.gender
            response['bloodGroup'] = student.bloodGroup
            response['dob'] = student.dob
            response['status'] = 1  # registered
        except:
            response['status'] = 2  # not registered
    return JsonResponse(response)


@csrf_exempt
def login(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        email = post['email']
        try:
            user = User.objects.get(email__iexact=email)
            student= Student.objects.get(user=user)
            password = randomString()
            user.set_password(password)
            user.save()
            response["password"]=password
            student.save()
            #student.roll = post['roll']
            #student.name = post['name']
            #student.phone = post['phone']
            #student.department = post['department']
            #student.fcmtoken = post['fcmtoken']
            #student.year = post['year']
            response['status'] = 2
        except:
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername
                    + 1))
            student = Student(user=user, email=email)
            #student.roll = int(post['roll'])
            #student.name = post['name']
            #student.phone = post['phone']
            #student.department = post['department']
            #student.fcmtoken = post['fcmtoken']
            #student.year = post['year']
            #user.first_name = post['name']
            password = randomString()
            user.set_password(password)
            user.save()
            response["password"]=password
            student.save()
            response['status'] = 1
    return JsonResponse(response)


# noinspection PyInterpreter

@csrf_exempt
def feedandclubs(request):
    response = {}
    response['status'] = 0
    response['councils'] = clubsandcouncils()['councils']
    try:
        if request.method == 'POST':
            post = json.loads(request.body)  # request.POST
            email = post['email']
            user = User.objects.get(email__iexact=email)
            if not user.check_password(post['password']):
                    print("wrong pswd")
                    raise Exception
            student= Student.objects.get(user=user)
            notifs = Notification.objects.all()

            # print(notifs.viewedby_set.all())

            if user.check:
                for notif in notifs:

                    # try:

                    if not student in notif.viewedby.all():
                        notif.viewedby.add(student)
                        notif.save()

                            # print("2132133333333333333333333333333333333333333333333333")
                    # except:
                    #         notif.viewedby.add(student)
                    #         notif.save()

                outnotif = []

                for notif in notifs:
                    curr = {}
                    curr['club'] = notif.clubname.name
                    if notif.clubname.clubimage:
                        curr['clubimage'] = notif.clubname.clubimage.url
                    curr['council'] = notif.clubname.councilname.name
                    if notif.clubname.councilname.image:
                        curr['councilimage'] = \
                            notif.clubname.councilname.image.url
                    curr['title'] = notif.notification_header
                    curr['description'] = notif.notification
                    if notif.notification_pic:
                        curr['image'] = notif.notification_pic.url
                    curr['datetime'] = notif.datetime
                    curr['location'] = notif.location
                    curr['map_location'] = notif.map_location
                    curr['viewedcount'] = notif.viewedby.count()
                    curr['interestedcount'] = notif.interested.count()
                    if notif.interested.count() <5:
                        curr["interested_names"] = [i.name for i in notif.interested.order_by('?')[:notif.interested.count()]]
                    else:
                        curr["interested_names"] = [i.name for i in notif.interested.order_by('?')[:5]]

                    if student in notif.interested.all():
                        curr['interested'] = 1
                    else:
                        curr['interested'] = 0

                    curr['notifid'] = notif.id
                    outnotif.append(curr)

                response['status'] = 1
                response['notif'] = outnotif
                print(response)
                return JsonResponse(response)
            else:

                return JsonResponse(response)
    except Exception as e:
        print(e)
        return JsonResponse(response)
    return JsonResponse(response)


@csrf_exempt
def postcomplain(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        print (request.body)
        post = json.loads(request.body)  # request.POST
        try:
            user = User.objects.get(email__iexact=email)
            if not user.check_password(post['password']):
                    raise Exception
            student= Student.objects.get(user=user)
        except:
            return JsonResponse(response)
        student= Student.objects.get(user=user)
        if student:
            complainheader = post['header']
            complaintype = post['type']
            if post['anonymous']:
                complain = Complain(complain=post['complain'])
                complain.complainheader = complainheader
                if 'hostel' in post:
                    complainsubtype = post['hostel']
                    complain.complainsubtype = complainsubtype
                complain.complaintype = complaintype
                complain.save()
            else:

                complain = Complain(complain=post['complain'],
                                    complainby=student)
                complain.complainheader = complainheader
                if 'hostel' in post:
                    complainsubtype = post['hostel']
                    complain.complainsubtype = complainsubtype
                complain.complaintype = complaintype
                complain.save()

            response['status'] = 1
            print(response)
            return JsonResponse(response)
        else:

            return JsonResponse(response)

    return JsonResponse(response)


@csrf_exempt
def interested(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        user = User.objects.get(email__iexact=post['email'])
        student = Student.objects.get(user=user)
        print (student)
        if student:
            notif = Notification.objects.get(id=int(post['notifid']))
            response["intrested_names"] = [i.name for i in list(notif.interested.all())]
            print(interested)
            if notif:
                if not student in notif.interested.all():
                    notif.interested.add(student)
                    notif.save()
                    response['status'] = 1
                else:
                    response['status'] = 2

                return JsonResponse(response)

    return JsonResponse(response)


def clubsandcouncils():
    response = {}
    response['councils'] = []
    clubs = Club.objects.all()
    for c in clubs:
        club = {}
        club['name'] = c.name
        if c.clubimage:
            club['image'] = c.clubimage.url
        flag = 1
        for councilds in response['councils']:
            if councilds['name'] == c.councilname.name:
                councilds['clubs'].append(club)
                flag = 0
        if flag:
            cou = {}
            cou['name'] = c.councilname.name
            if c.councilname.image:
                cou['image'] = c.councilname.image.url
            cou['clubs'] = []
            cou['clubs'].append(club)
            response['councils'].append(cou)
    return response
@csrf_exempt
def timetable(request):
    response = {}
    response['status'] = 0

    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        email = post['email']
        try:
             user = User.objects.get(email__iexact=email)
             if not user.check_password(post['password']):
                    raise Exception
             student = Student.objects.get(user=user)
             dept = student.department
             timetable = TimeTable.objects.get(department = dept)
             response['image'] = timetable.tableimage.url
             response['status'] = 1
        except:
            response['status'] =2

        return JsonResponse(response)

@csrf_exempt
def importantcontacts(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        contacts = ImpContact.objects.all()
        response['data'] = [
            {
                "name" : contact.name,
                "email" : contact.email,
                "phone" : contact.phone,
                "role" : contact.role_type,
            } for contact in contacts ]
        response['status'] = 1
    return JsonResponse(response)

@csrf_exempt
def pors(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
         post = json.loads(request.body)  # request.POST
         pors = POR.objects.all()
         response['data'] = [
             {
                 "name" : por.name,
                 "email" : por.email,
                 "council" : por.councilname,
                 "position" : por.postion,
                 "phone":por.phone,
                 "department":por.dept,
                 "responsibility":por.responsibility,
                 "image":por.image.url
             } for por in pors ]
         response['status'] = 1
    return JsonResponse(response)


@csrf_exempt
def notification(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = json.loads(request.body)
        print(post)
        try:
           user = User.objects.get(email__iexact=post['email'])
           if user.check_password(post['password']):
                club =  Club.objects.get(name = post['club'])
                notif = Notification.objects.create(clubname = club)
                notif.datetime = datetime.datetime(post['year'],post['month'],post['day'],post['hour'],post['minutes'],0,0,tzinfo = timezone.utc)
                notif.notification_header = post['header']
                notif.notification = post['description']
                notif.location = post['location']
                notif.map_location = post['map_location']
                notif.notification_pic = File(b64decode(post['image'].encode("utf8")))
                notif.save()
                jsondata = {"notification": {"title": post["header"],"body" : post["description"],"location":post['location'],"year":post['year'],"month":post["month"],"hour":post['hour'],"minutes":post['minutes']},"to": "/topics/"+ post["club"].split()[0]}
                firebase_messaging_req =req.post(url="https://fcm.googleapis.com/fcm/send",data=json.dumps(jsondata),headers = {"Content-Type":"application/json","Authorization":"key=AAAAIJ0yPMw:APA91bFSHkaDO3-s5c6K3U8H0LQFrU7PUz1GIMlaW5lit6dtsh46JUgvJD_cT0l79P_pJQRfeoqs57WjG9DqMdVFpglDjBl9CnZ_lINpmo7AQxol6p7U0BdpPEbh5M2PTpiCiZdx7vOP"})
                print(firebase_messaging_req.json())
           else:
                response['status']=3
                return JsonResponse(response)

        except Exception as e:
            print("error:",e)
            return JsonResponse(response)
        response['status'] = 1
    return JsonResponse(response)

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.files import File
import json
import requests as req
from base64 import *
from django.utils import timezone
import string
import random
import datetime

def randomString(stringLength=10):
    """Generate a random string of fixed length """

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@csrf_exempt
def checkregister(request):

    response = {}
    response['status'] = 0

    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        email = post['email']
        try:
            user = User.objects.get(email__iexact=email)
            if not user.check_password(post['password']):
                    raise Exception
            student= Student.objects.get(user=user)
            response['name'] = student.name
            response['roll'] = student.roll
            response['phone'] = student.phone
            response['department'] = student.department
            response['yearOfAdmission'] = student.yearOfAdmission
            response['course'] = student.course
            response['fatherName'] = student.fatherName
            response['address'] = student.address
            response['gender'] = student.gender
            response['bloodGroup'] = student.bloodGroup
            response['dob'] = student.dob
            response['status'] = 1  # registered
        except:
            response['status'] = 2  # not registered
    return JsonResponse(response)


@csrf_exempt
def login(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        email = post['email']
        try:
            user = User.objects.get(email__iexact=email)
            student= Student.objects.get(user=user)
            password = randomString()
            user.set_password(password)
            user.save()
            response["password"]=password
            student.save()
            #student.roll = post['roll']
            #student.name = post['name']
            #student.phone = post['phone']
            #student.department = post['department']
            #student.fcmtoken = post['fcmtoken']
            #student.year = post['year']
            response['status'] = 2
        except:
            bugUsername = User.objects.latest('id').id
            user = User.objects.create_user(username=str(bugUsername
                    + 1))
            student = Student(user=user, email=email)
            #student.roll = int(post['roll'])
            #student.name = post['name']
            #student.phone = post['phone']
            #student.department = post['department']
            #student.fcmtoken = post['fcmtoken']
            #student.year = post['year']
            #user.first_name = post['name']
            password = randomString()
            user.set_password(password)
            user.save()
            response["password"]=password
            student.save()
            response['status'] = 1
    return JsonResponse(response)


# noinspection PyInterpreter

@csrf_exempt
def feedandclubs(request):
    response = {}
    response['status'] = 0
    response['councils'] = clubsandcouncils()['councils']
    try:
        if request.method == 'POST':
            post = json.loads(request.body)  # request.POST
            email = post['email']
            user = User.objects.get(email__iexact=email)
            if not user.check_password(post['password']):
                    print("wrong pswd")
                    raise Exception
            student= Student.objects.get(user=user)
            notifs = Notification.objects.all()

            # print(notifs.viewedby_set.all())

            if user.check:
                for notif in notifs:

                    # try:

                    if not student in notif.viewedby.all():
                        notif.viewedby.add(student)
                        notif.save()

                            # print("2132133333333333333333333333333333333333333333333333")
                    # except:
                    #         notif.viewedby.add(student)
                    #         notif.save()

                outnotif = []

                for notif in notifs:
                    curr = {}
                    curr['club'] = notif.clubname.name
                    if notif.clubname.clubimage:
                        curr['clubimage'] = notif.clubname.clubimage.url
                    curr['council'] = notif.clubname.councilname.name
                    if notif.clubname.councilname.image:
                        curr['councilimage'] = \
                            notif.clubname.councilname.image.url
                    curr['title'] = notif.notification_header
                    curr['description'] = notif.notification
                    if notif.notification_pic:
                        curr['image'] = notif.notification_pic.url
                    curr['datetime'] = notif.datetime
                    curr['location'] = notif.location
                    curr['map_location'] = notif.map_location
                    curr['viewedcount'] = notif.viewedby.count()
                    curr['interestedcount'] = notif.interested.count()
                    if notif.interested.count() <5:
                        curr["interested_names"] = [i.name for i in notif.interested.order_by('?')[:notif.interested.count()]]
                    else:
                        curr["interested_names"] = [i.name for i in notif.interested.order_by('?')[:5]]

                    if student in notif.interested.all():
                        curr['interested'] = 1
                    else:
                        curr['interested'] = 0

                    curr['notifid'] = notif.id
                    outnotif.append(curr)

                response['status'] = 1
                response['notif'] = outnotif
                print(response)
                return JsonResponse(response)
            else:

                return JsonResponse(response)
    except Exception as e:
        print(e)
        return JsonResponse(response)
    return JsonResponse(response)


@csrf_exempt
def postcomplain(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        print (request.body)
        post = json.loads(request.body)  # request.POST
        try:
            user = User.objects.get(email__iexact=email)
            if not user.check_password(post['password']):
                    raise Exception
            student= Student.objects.get(user=user)
        except:
            return JsonResponse(response)
        student= Student.objects.get(user=user)
        if student:
            complainheader = post['header']
            complaintype = post['type']
            if post['anonymous']:
                complain = Complain(complain=post['complain'])
                complain.complainheader = complainheader
                if 'hostel' in post:
                    complainsubtype = post['hostel']
                    complain.complainsubtype = complainsubtype
                complain.complaintype = complaintype
                complain.save()
            else:

                complain = Complain(complain=post['complain'],
                                    complainby=student)
                complain.complainheader = complainheader
                if 'hostel' in post:
                    complainsubtype = post['hostel']
                    complain.complainsubtype = complainsubtype
                complain.complaintype = complaintype
                complain.save()

            response['status'] = 1
            print(response)
            return JsonResponse(response)
        else:

            return JsonResponse(response)

    return JsonResponse(response)


@csrf_exempt
def interested(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        user = User.objects.get(email__iexact=post['email'])
        student = Student.objects.get(user=user)
        print (student)
        if student:
            notif = Notification.objects.get(id=int(post['notifid']))
            response["intrested_names"] = [i.name for i in list(notif.interested.all())]
            print(interested)
            if notif:
                if not student in notif.interested.all():
                    notif.interested.add(student)
                    notif.save()
                    response['status'] = 1
                else:
                    response['status'] = 2

                return JsonResponse(response)

    return JsonResponse(response)


def clubsandcouncils():
    response = {}
    response['councils'] = []
    clubs = Club.objects.all()
    for c in clubs:
        club = {}
        club['name'] = c.name
        if c.clubimage:
            club['image'] = c.clubimage.url
        flag = 1
        for councilds in response['councils']:
            if councilds['name'] == c.councilname.name:
                councilds['clubs'].append(club)
                flag = 0
        if flag:
            cou = {}
            cou['name'] = c.councilname.name
            if c.councilname.image:
                cou['image'] = c.councilname.image.url
            cou['clubs'] = []
            cou['clubs'].append(club)
            response['councils'].append(cou)
    return response
@csrf_exempt
def timetable(request):
    response = {}
    response['status'] = 0

    if request.method == 'POST':
        post = json.loads(request.body)  # request.POST
        email = post['email']
        try:
             user = User.objects.get(email__iexact=email)
             if not user.check_password(post['password']):
                    raise Exception
             student = Student.objects.get(user=user)
             dept = student.department
             timetable = TimeTable.objects.get(department = dept)
             response['image'] = timetable.tableimage.url
             response['status'] = 1
        except:
            response['status'] =2

        return JsonResponse(response)

@csrf_exempt
def importantcontacts(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        contacts = ImpContact.objects.all()
        response['data'] = [
            {
                "name" : contact.name,
                "email" : contact.email,
                "phone" : contact.phone,
                "role" : contact.role_type,
            } for contact in contacts ]
        response['status'] = 1
    return JsonResponse(response)

@csrf_exempt
def pors(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
         post = json.loads(request.body)  # request.POST
         pors = POR.objects.all()
         response['data'] = [
             {
                 "name" : por.name,
                 "email" : por.email,
                 "council" : por.councilname,
                 "position" : por.postion,
             } for por in pors ]
         response['status'] = 1
    return JsonResponse(response)


@csrf_exempt
def notification(request):
    response = {}
    response['status'] = 0
    if request.method == 'POST':
        post = json.loads(request.body)
        print(post)
        try:
           user = User.objects.get(email__iexact=post['email'])
           if user.check_password(post['password']):
                club =  Club.objects.get(name = post['club'])
                notif = Notification.objects.create(clubname = club)
                notif.datetime = datetime.datetime(post['year'],post['month'],post['day'],post['hour'],post['minutes'],0,0,tzinfo = timezone.utc)
                notif.notification_header = post['header']
                notif.notification = post['description']
                notif.location = post['location']
                notif.map_location = post['map_location']
                notif.notification_pic = File(b64decode(post['image'].encode("utf8")))
                notif.save()
                jsondata = {"notification": {"title": post["header"],"body" : post["description"],"location":post['location'],"year":post['year'],"month":post["month"],"hour":post['hour'],"minutes":post['minutes']},"to": "/topics/"+ post["club"].split()[0]}
                firebase_messaging_req =req.post(url="https://fcm.googleapis.com/fcm/send",data=json.dumps(jsondata),headers = {"Content-Type":"application/json","Authorization":"key=AAAAIJ0yPMw:APA91bFSHkaDO3-s5c6K3U8H0LQFrU7PUz1GIMlaW5lit6dtsh46JUgvJD_cT0l79P_pJQRfeoqs57WjG9DqMdVFpglDjBl9CnZ_lINpmo7AQxol6p7U0BdpPEbh5M2PTpiCiZdx7vOP"})
                print(firebase_messaging_req.status_code)
           else:
                response['status']=3
                return JsonResponse(response)

        except Exception as e:
            print("error:",e)
            return JsonResponse(response)
        response['status'] = 1
    return JsonResponse(response)
