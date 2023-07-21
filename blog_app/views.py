from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog_app.forms import UserAddForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from.models import Bloglist
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage




# Create your views here.
def first(request):
    
    return HttpResponse("hello world")

def home(request):

    return render(request,"home.html")

def signup(request):
    form=UserAddForm()
    if request.method=='POST':
        form=UserAddForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            username=form.cleaned_data.get("username")
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name is already taken")
                return redirect("signup")
            if User.objects.filter(email=email).exists():
                messages.info(request,"email is alredy taken")
                return redirect("signup")
            else:
                newUser=form.save()
                newUser.save()
                messages.info(request,"newUser created")
                return redirect("signin")
    return render(request,"register.html",{"form":form})


def signin(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request.session["username"]=username
            request.session["password"]=password
            login(request,user)
            return redirect("home")
        else:
            messages.info(request,"username or password is incorrect")
            return redirect("signin")
    return render(request,"login.html")



#  logout  signout

def signout(request):
    logout(request)
    return redirect("signin")
    

# blog.html

def blogpage(request):
    blogs=Bloglist.objects.all().order_by( "-Publish_date")

    # pagination

    p=Paginator(blogs,5)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj=p.page(1)
    except EmptyPage:
        page_obj=p.page(p.num_pages)


   
    return render(request,"blog.html",{"page_obj": page_obj})

# addblog
def addblog(request):
     if request.method=='POST':
        blog=Bloglist(Author_name=request.POST["Author_name"],Publish_date=request.POST["Publish_date"],Blog_title=request.POST["Blog_title"],Blog_caption=request.POST["Blog_caption"])
        blog.Blog_img=request.FILES.get("Blog_img")
        blog.Blog_category=request.POST.get("Blog_category")
        blog.save()
        messages.info(request,"successfully added")
        return redirect("blogpage")
     return render(request,"addblog.html")



    #  delete
def deleteblog(request,pk):
    item=Bloglist.objects.get(Blog_id=pk)
    item.delete()
    messages.info(request,"deleted")
    return redirect("blogpage")



        # editblog

def editpage(request, vid):
    single_blog = Bloglist.objects.get(Blog_id=vid)

    if request.method == "POST":
        single_blog.Blog_title = request.POST["Blog_title"]
        single_blog.Blog_caption = request.POST["Blog_caption"]
        single_blog.Blog_category = request.POST["Blog_category"]
        if "Blog_img" in request.FILES:
            single_blog.Blog_img = request.FILES["Blog_img"]
        single_blog.save()
        return redirect("viewmyblog")

    # For GET request, pre-populate the form fields with the data from single_blog
    return render(request, "editblog.html", {"single_blog": single_blog})

        
    

   
    #     Bloglist.objects.filter(Blog_id=vid).update(Blog_title=request.POST["Blog_title"],Blog_caption=request.POST["Blog_caption"]),
       
    # single_blog=Bloglist.objects.get(Blog_id=vid)
   


   # view myblog.html
def viewmyblog(request):
    myblogs=Bloglist.objects.filter(Author_name=request.user.username)
    print(myblogs)
    return render(request,"viewmyblog.html",{"myblogs":myblogs})



# like
def like(request,Blog_id):
    blog=get_object_or_404(Bloglist,Blog_id=Blog_id)
    if request.method=="POST":
        if request.user in blog.likes.all():
            blog.likes.remove(request.user)
        else:
            blog.likes.add(request.user)





    return redirect("blogpage")


# video.html

def videoblog(request):

    return render(request,"video.html")








    


