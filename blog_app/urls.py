from django.urls import path
from.import views 


urlpatterns = [
    path('',views.first,name='first'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('blogpage/',views.blogpage,name='blogpage'),
    path('addblog/',views.addblog,name="addblog"),
    path('deleteblog/<int:pk>',views.deleteblog,name="deleteblog"),

    path('signout',views.signout,name="signout"),
    path('viewmyblog',views.viewmyblog,name="viewmyblog"),
    path('editpage/<int:vid>',views.editpage,name="editpage"),
    path('like/<int:Blog_id>/like/',views.like,name="like"),
    path('videoblog/',views.videoblog,name='videoblog'),
   
]