from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

from blog.models import Post

# Create your views here.

from django.http import HttpResponse

from blog.forms import PostForm

@login_required(login_url='/login/')
@csrf_protect
def show_index(request):
    user = User.objects.get(username='kamal')
    context = {}

    if request.method == 'POST':
        form = PostForm(request.POST)
        context['form'] = form
        #import pdb;pdb.set_trace()
        if form.is_valid():
            request.session['form_valid'] = username
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            post = Post(title=title, text=text)
            post.author = user
            post.save()

            return redirect('/posts/')
    else:
        form = PostForm()
        context['form'] = form

    posts = Post.objects.all()
    context['posts'] = posts

    #return HttpResponse(json.dumps(data), content_type='application/json')
    return render(request, 'posts.html', context)

def show_user(request):
    username = request.GET.get('username', None)
    if request.session.get('form_valid', False):
        pass

    if username is not None:
        users = User.objects.filter(username=username)
    else:
        users = User.objects.all()

    return render(request, 'users.html', {'users': users})
