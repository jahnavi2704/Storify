from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import *
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login
from django.views.generic import FormView,View,ListView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView,DetailView
from .models import *

from rest_framework import viewsets
from .serializers import genreserializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


def usersignup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('mainapp/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),#.decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
    else:
        form = UserSignUpForm()
    return render(request, 'mainapp/login.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request,'mainapp/index.html')

    else:
        return HttpResponse('Activation link is invalid!')

def homepage(request):
    article2=articles.objects.all()[:2]
    article=articles.objects.all()[2:]
    comments_order=articles.objects.order_by('upvotes')[:5]
    genres=genre.objects.all()
    #print(genres)
    # titles=[]
    # print(comments_order)
    # for aid in comments_order :
    #     print(aid.articleId)
    #     for a in article:
    #         print(a.articleId)
    #         if (aid.articleId==a.articleId):
    #             print('-------------------------')
    #             titles.append(a.title)

    return render(request, 'mainapp/index.html',{'comments_order':comments_order,'genres':genres,'article':article,'article2':article2})



def detail_article(request):
    genres=genre.objects.all()
    if request.method=="POST":

        a=request.POST.get('aname')
        #print(a)

        article1=articles.objects.get(title=a)
        #c=comments.objects.get(articleId=article1.title)
        print(article1)
    return render(request,'mainapp/single-post.html',{'object':article1,'genres':genres})

#def genre_display(request):
def comments_show(request):

    user=request.user
    print(user)
    usero=userInfo.objects.get(userId=user)
    if request.method=="POST":
        a=request.POST.get('aname')
        print(a)
        ao=articles.objects.get(title=a)
        c=request.POST.get('message')
        comments.objects.create(articleId=ao,comment_data=c,userId=user)


    return render(request,'mainapp/single-post.html')

@login_required(login_url='mainapp/login')
def UpdateProfile(request):
    if request.method == 'POST':
        print("dgljiglkgjlkjfjd;j---------------------------------------")
        form_1 = ProfileUpdateForm(request.POST)
        print(form_1)
        if  form_1.is_valid():
            print("bjkkgjk,b---------------------------------------------,")
            # user_image = form_1.cleaned_data.get('display_pic')
            # user_username = form_1.cleaned_data.get('user')
            # user_name = form_1.cleaned_data.get('name')
            # user_birthday = form_1.cleaned_data.get('dateofbirth')
            # user_profession = form_1.cleaned_data.get('profession')
            # user_gender = form_1.cleaned_data.get('gender')
            user = User.objects.get(username=request.user.username)
            profile = form_1.save(commit = False)
            profile.user = user
            profile.save()
            print('jaaaahnviiii')
            return render(request, 'mainapp/index.html')
        else:
            return render(request, 'mainapp/index.html')
    else:
        print ("inside else condition")
        form_1 = ProfileUpdateForm()
        if request.user.is_authenticated:
            user_values = request.user
            
        context = {'dict_user': user_values, 'profile_form': form_1}
        return render(request, 'mainapp/submit-video.html', context)

@api_view(['GET'])
def articlelist(request):
    if request.method == 'GET':
       reqgenre= request.GET['genrepassed']
       articles_all=articles.objects.filter(Q(genre__genre__contains = reqgenre))
       serializer=genreserializer(articles_all,many=True)
       return Response(serializer.data)




