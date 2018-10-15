from django.conf.urls import url
from home import views


app_name="home"
urlpatterns =[
    url(r'^$',views.index,name = 'home'),
    url(r'^about/$',views.about,name = 'about'),
    url(r'^contact/$',views.contact,name = 'contact'),
    url(r'^message/',views.message,name='message'),
]
