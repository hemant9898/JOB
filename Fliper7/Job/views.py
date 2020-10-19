from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .models import *
from django.core.serializers import serialize
# Create your views here.
joke={'1','2','3','4','5','6','7','8','9','10'}

def LR(request):
	return render(request,"Job/LR.html")



def home(request):
	jj=data.objects.all()
	paginator = Paginator(jj,4)

	try:
		page = int(request.GET.get('page',1))
	except:
		page=1

	try:
		posts = paginator.page(page)
	except(EmptyPage):
		posts = paginator.page(paginator,num_pages)

	return render(request,'Job/home.html',{
		'posts':posts,
		})
	


def filter(request):
	is_cookie_set = 0
	if request.method == "POST":
		datas = data.objects.all()

		if request.POST["exp"]:
			experience = int(request.POST["exp"])
			datas = datas.filter(exp__range = (0,experience))


		if request.POST["loc"]:
			location = request.POST["loc"]
			datas = datas.filter(loc = location)


		if request.POST["skill"]:
			skills = request.POST["skill"]
			datas = datas.filter(skill = skills)


		if request.POST["indus"]:
			industory = request.POST["indus"]
			datas = datas.filter(indus = industory)


		if request.POST["salary"]:
			Salary = int(request.POST["salary"])
			datas = datas.filter(salary__range = (0,Salary))

		return render(request,'Job/test.html',{
			'posts':datas,
			})
	return render(request, "Job/filter.html")
		

	



def filtered(request):
	paginator = Paginator(DATA,2)
	try:
		page = int(request.GET.get('page',1))
	except:
		page=1

	try:
		posts = paginator.page(page)
	except(EmptyPage):
		posts = paginator.page(paginator,num_pages)

	return render(request,'Job/test.html',{
		'posts':posts,
		})






def test(request):
	jj=data.objects.all()
	paginator = Paginator(jj,4)

	try:
		page = int(request.GET.get('page',1))
	except:
		page=1

	try:
		posts = paginator.page(page)
	except(EmptyPage):
		posts = paginator.page(paginator,num_pages)

	return render(request,'Job/test.html',{
		'posts':posts,
		})



def login_view(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["password"]
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return HttpResponseRedirect(reverse("Job:home"))
		else:
			return render(request, "Job/LR.html",{
				"m": "Invalid"
				})
	return render(request,"Job/LR.html")



def reg_view(request):
	if request.method == "POST":
		username=request.POST["username"]
		password=request.POST["password"]
		email = request.POST["email"]
		rpassword = request.POST["rpassword"]
		if password == rpassword:
			user=User(username=username,password=password,email=email)
			user.save()
			return render(request, "Job/LR.html")
		else:
			return render(request, "Job/LR.html",{
				"msg":"INVALID"
				})
	return render(request, "Job/LR.html")



def logout_view(request):
	logout(request)
	return render(request, "Job/LR.html")



	
	
def jsp(request, user_id, data_id):
	datas = data.objects.get(pk=data_id)
	user = User.objects.get(pk=user_id)
	datas.user.add(user)

	jj=data.objects.all()
	paginator = Paginator(jj,4)

	try:
		page = int(request.GET.get('page',1))
	except:
		page=1

	try:
		posts = paginator.page(page)
	except(EmptyPage):
		posts = paginator.page(paginator,num_pages)

	return render(request,'Job/home.html',{
		'posts':posts,
		'user':user
		})


def user_job(request, user_id):
	jj=data.objects.filter(user=user_id)
	user = User.objects.get(pk=user_id)

	paginator = Paginator(jj,4)

	try:
		page = int(request.GET.get('page',1))
	except:
		page=1

	try:
		posts = paginator.page(page)
	except(EmptyPage):
		posts = paginator.page(paginator,num_pages)

	return render(request,'Job/seeking.html',{
		'posts':posts,
		'user':user
		})