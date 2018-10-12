from django.urls import path,include
from todo.views import MyNewView,MyView,MyLoginView,MySignUpView,LogoutView,ExampleView
from django.contrib.auth.decorators import login_required
#from . import views
from django.views.generic.base import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views



urlpatterns = [
	path('item/', MyView.as_view(), name='my_view') ,
	path('item_new/', MyNewView.as_view(),name='todo_new'),
	path('login/',MyLoginView.as_view(),name='login'),
	#path('login/',auth_views.login),
	#path('login/', include('django.contrib.auth.urls')),
	#path('logout/',views.logout_view,name="logout"),
	path('logout/',LogoutView.as_view(),name='logout'),
	path('signup/',MySignUpView.as_view(),name='signup'),
	path('api-token-auth/',views.obtain_auth_token,name='api-token-auth'),
	path('accounts/', include('rest_registration.api.urls')),
	path('example/',ExampleView.as_view(),name='example'),
	#path('', TemplateView.as_view(template_name='index1.html'), name='index1'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
