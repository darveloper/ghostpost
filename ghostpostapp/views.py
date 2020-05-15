from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpostapp.models import BR
from ghostpostapp.forms import BRForm
from datetime import datetime 

def index(request):
    posts = BR.objects.all().order_by('-timestamp')
     
    return render(request, 'index.html', { 'posts': posts })

def createpost(request):
    if request.method == "POST":
        form = BRForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            BR.objects.create(
                post = data['textinput'],
                is_boast = data['is_boast']
            )
            return HttpResponseRedirect(reverse('homepage'))
        
    form = BRForm()

    return render(request, 'post.html', {'form': form })

def up_votes(request, id):
    
    post = BR.objects.get(id=id)
    post.upvote += 1
    post.total_votes += 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def down_votes(request, id):
    
    post = BR.objects.get(id=id)
    post.downvote += 1
    post.total_votes -= 1
    post.save()
    return HttpResponseRedirect(reverse('homepage'))

def boast(request):
    html = 'boasts.html'
    posts = BR.objects.all().filter(is_boast=True).order_by('-timestamp')
    return render(request, html, {'posts': posts})


def roast(request):
    html = 'roasts.html'
    posts = BR.objects.all().filter(is_boast=False).order_by('-timestamp')
    return render(request, html, {'posts': posts})

def sortedby_posts(request):
    posts = BR.objects.order_by('-total_votes')
    return render(request, 'sorted.html', {'posts': posts})
    