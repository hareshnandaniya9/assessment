from django.shortcuts import render,redirect
from .models import Feedback,User
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def index(request):
	return render(request,"index.html")

def feedback(request):
	if request.method=="POST":
		Feedback.objects.create(
			name=request.POST["name"],
			email=request.POST["email"],
			mobile=request.POST["mobile"],
			feedback=request.POST["feedback"]
			)
		msg="Your Contect Saved Successfuly"
		feedbacks=Feedback.objects.all().order_by("-id")[:5]
		return render(request,"feedback.html",{'msg':msg,'feedbacks':feedbacks})

	else:
		feedbacks=Feedback.objects.all().order_by("-id")[:5]
		return render(request,"feedback.html",{'feedbacks':feedbacks})

def signup(request):
	if request.method=="POST":
		user=User()
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']
		user.mobile=request.POST['mobile']
		user.gender=request.POST['gender']
		user.dob=request.POST['dob']
		user.aadhaar=request.POST['aadhaar']
		user.state=request.POST['state']
		user.city=request.POST['city']
		user.pincode=request.POST['pincode']
		user.address=request.POST['address']
		user.password=request.POST['password']
		# user.photo=request.POST['photo']

		try:
			User.objects.get(email=request.POST['email'])
			msg="Email Alredy Resister"
			return render(request,"signup.html",{'msg':msg,'user':user})
		except:
			try:
				User.objects.get(mobile=request.POST['mobile'])
				msg="Mobile Number Alredy Resister"
				return render(request,"signup.html",{'msg':msg,'user':user})
			except:



				if request.POST['password']==request.POST['cpassword']:
					User.objects.create(
						fname=request.POST['fname'],
						lname=request.POST['lname'],
						email=request.POST['email'],
						mobile=request.POST['mobile'],
						gender=request.POST['gender'],
						dob=request.POST['dob'],
						aadhaar=request.POST['aadhaar'],
						state=request.POST['state'],
						city=request.POST['city'],
						pincode=request.POST['pincode'],
						address=request.POST['address'],
						password=request.POST['password'],
						photo=request.FILES['photo']
						)
					msg="Your Acount Created Successfuly"
					return render(request,"signup.html",{'msg':msg})

				else:
					msg="Password & Confrim Password Does Not Matched"
					return render(request,"signup.html",{'msg':msg,'user':user})
	else:
		return render(request,"signup.html")
def login(request):
	if request.method=="POST":

		try:
			user=User.objects.get(email=request.POST['email'])
			if user.password==request.POST['password']:
				request.session['email']=user.email
				request.session['fname']=user.fname
				request.session['lname']=user.lname
				request.session['photo']=user.photo.url

				return render(request,"index.html")

			else:
				msg="Password Does Not Matched"
				return render(request,"login.html",{'msg':msg})
		except:
			msg="Email Does Not Matched"
			return render(request,"login.html",{'msg':msg})
	else:
		return render(request,"login.html")

def logout(request):
	try:
		del request.session['email']
		del request.session['fname']
		del request.session['lname']
		del request.session['photo']

		return render(request,"login.html")
	except:
		return render(request,"login.html")
def change_password(request):

	if request.method=="POST":

		user=User.objects.get(email=request.session['email'])

		if user.password==request.POST['old_password']:

			if request.POST['newpassword']==request.POST['cnew_password']:

				user.password=request.POST['new_password']
				msg="Your Password Change Successfuly"
				del request.session['email']
				del request.session['fname']
				del request.session['lname']
				del request.session['photo']

				return render(request,"login.html",{'msg':msg})
			else:
				msg="Your New password & Confrim New Password Does Not Matched"
				return render(request,"change_password.html",{'msg':msg})
		else:
			msg="Your Old Password Does Not Matched"
			return render(request,"change_password.html",{'msg':msg})
	else:
		return render(request,"change_password.html")

def help(request):
	return render(request,"help.html")
def terms(request):
	return render(request,"terms.html")

def contect(request):
	return render(request,"contect.html")

def change_password(request):
	return render(request,"change_password.html")

def forget_password(request):
	if request.method=="POST":
		try:

			user=User.objects.get(email=request.POST['email'])
			otp=random.randint(1000,9999)
			subject = 'otp for forgote password'
			message = 'Dear, '+user.fname+" "+user.lname+",\n You have reqquested for a new password. \nOTP: "+str(otp) +"\n Don't Share any one Your OTP and Password \n Thank You"
			email_from = settings.EMAIL_HOST_USER
			recipient_list = [user.email, ]
			send_mail( subject, message, email_from, recipient_list )
			msg="OTP Sent"
			return render(request,"otp.html",{'otp':otp,'email':user.email,'msg':msg})


		except:

			msg="Your Email Not Resistered"
			return render(request,"forget_password.html",{'msg':msg})


	else:
		return render(request,"forget_password.html")


def verify_otp(request):
	otp=request.POST['otp']
	uotp=request.POST['uotp']
	email=request.POST['email']
	if otp==uotp:
		return render(request,"new_password.html",{'email':email})

	else:
		msg="OTP Does Not Matched"
		return render(request,"otp.html",{'msg':msg,'otp':otp,'email':email})


def update_password(request):
	email=request.POST['email']
	np=request.POST['new_password']
	cnp=request.POST['cnew_password']

	if np==cnp:
		user=User.objects.get(email=email)
		if user.password==np:
			msg="Sorry You Don't Use Your Old Password"
			return render(request,'new_password.html',{'msg':msg,'email':email})
		else:

			user.password=np
			user.save()
			msg="Your Password Change Successfuly"
			return render(request,"login.html",{'msg':msg})
	else:
		msg="New Password & Confrim New Password Does Not Matched"
		return render(request,"new_password.html",{'msg':msg,'email':email})

def Profile(request):
	user=User.objects.get(email=request.session['email'])
	if request.method=="POST":
		
		user.fname=request.POST['fname']
		user.lname=request.POST['lname']
		user.email=request.POST['email']

		user.mobile=request.POST['mobile']
		user.gender=request.POST['gender']
		user.dob=request.POST['dob']
		user.aadhaar=request.POST['aadhaar']
		user.state=request.POST['state']
		user.city=request.POST['city']
		user.pincode=request.POST['pincode']
		user.address=request.POST['address']
		try:
			user.photo=request.FILES['photo']
		except:
			pass
		user.save()
		request.session['fname']=user.fname
		request.session['lname']=user.lname
		request.session['photo']=user.photo.url
		return render(request,"Profile.html",{'user':user})



	else:
		return render(request,"Profile.html",{'user':user})
		














