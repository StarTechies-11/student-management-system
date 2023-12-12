
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    #login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

     #Profile Update
    path('Profile',views.PROFILE,name='profile'),
    path('Profile/update',views.PROFILE_UPDATE,name='profile_update'),

     # this is hod pannel
    path('HOD/Home',Hod_views.HOME,name='hod_home'),
    path('HOD/Student/Add',Hod_views.ADD_STUDENT,name='add_student'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
