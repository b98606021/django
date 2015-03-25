from django.shortcuts import render
from datetime import datetime
from trips.models import Post

# Create your views here.

from django.http import HttpResponse
def hello_world(req):
	# Render ：產生 HttpResponse 物件。
	# render(request, template_name, dictionary)
	return render(req,
		'hello_world.html',
		{'current_time':datetime.now()})

def home(req):
	# get all the posts
	post_list = Post.objects.all()
	return render(req,
		'home.html',
		{'post_list': post_list})

def post_detail(req, id):
	post = Post.objects.get(id=id)
	return render(req,
		'post.html',
		{'post':post})