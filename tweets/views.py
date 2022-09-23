from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from django.urls import reverse_lazy, reverse

import tweets
from .models import Tweet
from .forms import TweetForm, PictureForm

from cloudinary.forms import cl_init_js_callbacks

# Create your views here.

def index(request):
    
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())


    # Get all tweet, limit = 20
    tweets = Tweet.objects.all().order_by('-created_at')[:20]

    # Show
    return render(request, 'tweets.html',
                {'tweets': tweets})


def delete(request, tweet_id):
    tweet = Tweet.objects.get(id = tweet_id)
    tweet.delete()
    return HttpResponseRedirect('/')
    # output = 'TWEET ID is ' + str(tweet_id)
    # return HttpResponse('/')

def edit(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    form = TweetForm
    return render(request, 'edit.html', {'tweet': tweet, 'form': form})


def LikeView(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    new_value = tweet.likes + 1
    tweet.likes = new_value
    tweet.save()
    return HttpResponseRedirect('/')
