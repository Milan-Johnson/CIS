from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from aiCore.aiReply import genrateAnswer
# from .models import *



# from django.views.generic import ListView, DetailView
# import openai
# Create your views here.


def homepage(request):
    return render(request,'index.html')

def signuppage(request):
    if request.method == 'POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if User.objects.filter(username=uname).exists():
            messages.info(request,"username already exists")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"email taken")  
            return redirect('signup')           
        elif pass1!=pass2:
            messages.info(request,"passwords didn't match!!!")
            return redirect('signup')
        else:
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')



    return render(request,'signup.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('chat')
        else:
            messages.info(request,"username or password is incorrect!!!")
            return redirect('login')
        
    return render(request,'login.html')

# @login_required(login_url='login')
# def chatpage(request):
#     print("123")
#     if request.method == "GET":
#         print("1")
#         print(request.GET.get('userMessage'))
#     elif request.method == "POST":
#         print("2")

#     userMessage=request.GET.get('userMessage')
#     print(userMessage)
#     return render(request,'chat.html')

# def specific(request):
#     print("134")
#     return HttpResponse("list1")

# def getResponse(request):
#     print("145")
#     userMessage=request.POST.get('userMessage')
#     print(userMessage)
    # return HttpResponse(userMessage)

@login_required(login_url='login')
def chatpage(request):
    # qs = Student.objects.all()
    userMessageTxt = request.GET.get('userMessage')
    print(userMessageTxt)
    # return render(request, "search1.html")
    answerTxt=genrateAnswer(userMessageTxt)
    return render(request, "search1.html",{"question" : userMessageTxt, "answer" : answerTxt})


def LogoutPage(request):
    logout(request)
    return redirect('homepage')


def passresetpage(request):
    if request.method=='POST':
        premail=request.POST.get('email')
        npass=request.POST.get('prpass1')
        cpass=request.POST.get('prpass2')
        user=authenticate(request,email=premail)
        if npass!=cpass:
            return redirect('passreset')
        else:
            my_user=User.objects.update(cpass)
            my_user.save()
            return redirect('login')
    return render(request,'pr.html')



    

# openai.api_key = "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"
# def getResponse(userText):
#     prompt = f"User: {userText}\nBot: "
#     data = openai.Completion.create(
#         engine="davinci",
#         prompt=prompt,
#         temperature=0.5,
#         max_tokens=100,
#         n=1,
#         stop=None,
#         timeout=5,
#     )
#     data = data.choices[0].text.strip()
#     return data