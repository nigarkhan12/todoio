from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views import View
from .models import TodoItem
from django.shortcuts import render,redirect
from .forms import Todoform
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import View
from rest_framework.authtoken.models import Token


@method_decorator(login_required,name='dispatch')
class MyView(View):
	def get(self, request):
		context = {'items': TodoItem.objects.all()}
		return render(request, "todo/index1.html", context,)

	def post(self, request, *args, **kwargs):
		#import pdb; pdb.set_trace()
		data = request.POST.dict()
		title= data['title']
		notes = data.get('notes')
		reminder =data.get('reminder')
		t = TodoItem(title_text=title, notes=notes,reminder=reminder)
		t.save()
		context = {'items': TodoItem.objects.all()}
		return render(request, "todo/index1.html", context,)



@method_decorator(login_required, name='dispatch')
class MyNewView(View):
	def post(self,request):
		form = Todoform()
		return render(request,'todo/index1bootstrap.html',{'form':form})

	def get(self, request):
		form = Todoform()
		context = {'items': TodoItem.objects.filter(user=request.user), 'form': form}
		return render(request, "todo/index1bootstrap.html", context)



class MyLoginView(APIView):
	def post(self,request,format=None):
		print(12345678)
		content = {'abc': 1}
		title = "Login"
		data = request.data
		username =data.get("username")
		password = data.get("password")
		return Response(content)



class MySignUpView(APIView):
	permission_classes = ()

	def post(self,request,format=None):
		# import pdb; pdb.set_trace()
		data = request.data
		username = data.get('username')
		password = data.get('password')
		email = data.get('email')
		user = User.objects.create_user(username, email, password)
		token = Token.objects.create(user=user)
		return Response({'token': token.key})

class ExampleView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

# Class Based View for SignUp
'''class MySignUpView(View):
	def post(self,request):
		if request.method == 'POST':
			#import pdb; pdb.set_trace()
			data = request.POST.dict()
			username = data.get('username')
			password = data.get('password')
			email = data.get('email')
			user = User.objects.create_user(username, email, password)
			return redirect('todo_new')
		else:
			print("Password didn't match")
		return render(request, '/signup.html/', {'form': form})

	def get(self, request):
		print(8765)
		context = {}
		return render(request, "signup.html", context)

#"Function based view"#
def logout_view(request):
		return render(request,"registration/login1.html/")
		auth.logout(request)
'''

class LogoutView(View):
	def post(self,request,*args,**kwargs):
		logout(request)
		return redirect('todo_new',permanent=True)

	def get(self, request):
		logout(request)
		return redirect('todo_new')



'''## Class Based View- MyLoginView ##
class MyLoginView(View):
	def post(self,request):
		print(12345678)
		title = "Login"
		#import pdb; pdb.set_trace()
		data = request.POST.dict()
		username =data.get("username")
		password = data.get("password")
		#username = request.POST['username']
		#password = request.POST['password']
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request, user)
		else:
			print("Invalid Login")
		return redirect('todo_new')

	def get(self, request):
		print(8765)
		form = Todoform()
		context = {'items': TodoItem.objects.all(), 'form': form}
		return render(request, "registration/loginbootstrap.html/", context)
'''
