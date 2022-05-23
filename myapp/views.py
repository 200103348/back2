from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.views.decorators.csrf import *
from .forms import *
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.decorators.csrf import *

# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm']
        form = Logreg(request.POST)
        email_subject = 'Activate your account'
        email_body = render_to_string('myapp/cart.html')
        emaill=EmailMessage(subject=email_subject, body=email_body, from_email='200103348@stu.sdu.edu.kz', to=[email])
        if password1 == password2:
            if regis.objects.filter(username = username).exists():
                print('Username are already used')
                return redirect('/register/')
            else:
                form.save()
                print('user created')
                emaill.send()        
        else:
            print('password not matching...')
            return redirect('/register/')
        return redirect('/register/')
    else:
        return render(request, 'myapp/account.html')



@csrf_exempt
def signin(request):
    if request.method == 'POST':
        form = UsersLog(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        data = regis.objects.filter(username=username)
        for q in data:
            if q.password == password:
                return redirect('/in/')
    return redirect('/register/')



def page(request):
    return render(request, 'myapp/cart.html')



def newproject(request):
    var = MenPrize.objects.all()
    return render(request, 'myapp/newproject.html', {'var': var})



def form(request):
    post = Articles.objects.all()
    return render(request, 'myapp/form.html', {'post': post})



class NewsDetailView(DetailView):
    model = Articles
    template_name = 'myapp/details_view.html'
    context_object_name = 'article'



class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'myapp/news_home.html'

    form_class = ArticlesForm



def delete(request, id):
    al = Articles.objects.get(id=id)
    al.delete()
    return redirect("sportnews")



def olympics(request):
    summ = Summer.objects.all()
    win = Winter.objects.all()
    context = {'summ': summ, 'win': win}
    return render(request, 'myapp/olympics.html', context=context)



def tokyo(request):
    return render(request, 'myapp/tokyo.html')



def news_home(request):
    error = ' '
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sportnews')
        else:
            error = 'Form was uncorrect'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'myapp/news_home.html', data)



def show_post(request, post_id):
    post = get_object_or_404(Post, slug=post_id)
    context = {'post': post}
    return render(request, 'myapp/oop.html', context=context)