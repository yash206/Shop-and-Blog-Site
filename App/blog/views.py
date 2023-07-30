from email import message
from pyexpat.errors import messages
from webbrowser import get
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Contact,Blog,FAQ
from django.contrib.auth  import authenticate,  login, logout


def index(request):
    allBlogs = Blog.objects.all().order_by('-timestamp')
    blog = []
    for item in allBlogs:
        blog.append({'id':item.blog_id,'name':item.name,'message':item.message,'time':item.timestamp})
    return render(request, 'blog/index.html',{'blog':blog})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        contact = Contact(name=name, phone=phone, email=email, subject=subject, message=message)
        contact.save()
        thank = True
    return render(request, 'blog/contact.html',{'thank':thank})

def FAQs(request):
    allfaq = FAQ.objects.all()
    faq=[]
    for item in allfaq:
        faq.append({'id':item.FAQ_id,'question':item.question,'answer':item.answer})
    return render(request, 'blog/FAQs.html', {'faq':faq})


def post(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('firstname', '') + " " + request.POST.get('lastname', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        blog = Blog(name=name, email=email, message=message)
        blog.save()
        thank = True
    return render(request, 'blog/post.html',{'thank':thank})


def blogView(request, myid):
    blog = Blog.objects.filter(blog_id=myid)
    return render(request, 'blog/blogview.html',{'blog':blog[0]})


def searchMatch(query, item):
    if query in item.name.lower():
        return True
    else:
        return False


def search(request):
    query = request.GET.get('search')
    allBlogs = Blog.objects.filter(name__icontains=query).order_by('-timestamp')
    params = {'allBlogs': allBlogs, "msg": ""} 
    if len(allBlogs) == 0 or len(query) > 50:
        params = {'msg': "There is no blog posted with the "+query+" name . Please enter a valid name !!!"}
    return render(request, 'blog/search.html', params)

def handleSignup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
       
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('BlogHome')
        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('BlogHome')
        if (password!= password2):
             messages.error(request, " Passwords do not match")
             return redirect('BlogHome')
        if User.objects.filter(username = username).first():
            messages.error(request, "This username is already taken")
            return redirect('BlogHome')
       
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        message.success(request, 'Your account is successfully created !!')
        return redirect('BlogHome')
    else:
        return HttpResponse('404 Error Not Found')
    
def handleLogin(request):
    if request.method=="POST":
        
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user = authenticate(request,username=loginusername,password=loginpassword) 
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("BlogHome")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("BlogHome")

    return HttpResponse("404 Error Not found")

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('BlogHome')