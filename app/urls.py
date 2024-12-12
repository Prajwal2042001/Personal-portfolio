from app import views
from projectss import views as v
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('projects',v.read,name='projects'),
    path('contact',views.contact,name='contact'),
    path('start',views.start,name='start'),
    path('register',views.register,name='register'),
    path('login',views.login_user,name="login"),
    path('logout',views.logout_user,name="logout"),
    path('delete/<a>',views.delete,name='delete'),
    path('projectinsert',v.insert,name='pinsert'),
    path('deleteproject/<a>',v.delete,name='del'),
    path('update/<praju>',v.update,name='update'),

]

# urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)