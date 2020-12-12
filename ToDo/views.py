from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import ToDo, User
from django.contrib.auth.models import auth
from django.contrib import messages
from .forms import ToDoForm

# Create your views here.
def index(request, uid):
    # todo_List = ToDo.objects.order_by('uid')  # list from DB in admin
    todo_List = ToDo.objects.filter(uid=uid).order_by('id')
    user = User.objects.get(id=uid)
    form = ToDoForm()
    context = {'todo_list': todo_List, 'form': form, 'user': user}
    return render(request, 'todo/index.html', context)

@require_POST
def addToDo(request, uid):
    form = ToDoForm(request.POST)
    user = User.objects.get(id=uid)

    if form.is_valid():
        new_todo = ToDo(text=request.POST['text'], uid=user.id)
        new_todo.save()

    return redirect('index', uid=user.id)


@require_POST
def update_add(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)

    form = ToDoForm(request.POST)

    if form.is_valid():
        todo.text = request.POST['text']
        todo.save()
    return redirect('index', uid=todo.uid)


def completeToDo(request, todo_id, uid):
    todo = ToDo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index', uid=uid)


def deleteCompleted(request, uid):
    ToDo.objects.filter(complete__exact=True, uid=uid).delete()

    return redirect('index', uid=uid)

def deleteAll(request, uid):
    ToDo.objects.filter(uid=uid).all().delete()

    return redirect('index', uid=uid)


def update(request, uid):
    todo_List = ToDo.objects.filter(uid=uid).order_by('id')  # list from DB in admin
    context = {'todo_list': todo_List}
    return render(request, 'todo/update.html', context)


def updatetodo(request, todo_id):
    todo = ToDo.objects.get(pk=todo_id)
    form = ToDoForm()
    context = {'form': form, 'todo': todo}
    return render(request, 'todo/update_add.html', context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                print('Username already taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                print('Email already taken')
                return redirect('register')

            else:
                user = User(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()

                print('user registered...')
                return redirect('login')
        else:
            messages.info(request, 'password not matching...\n not registered...')
            print('password not matching...\n not registered...')
            return redirect('register')

        return redirect('login')

    else:
        return render(request, 'todo/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # user = auth.authenticate(username=username, password=password)

        user = User.objects.get(username=username)
        # context = {'uid': user.id}
        # u = user.id

        if user.username == username and user.password == password:
            # auth.login(request, user)
            # return render(request, 'todo/index.html', context)
            print(user.id)
            print(user.username)
            return redirect('index', uid=user.id)

        else:
            messages.info(request, 'invalid credentials')
            print('invalid credentials')
            return redirect('login')

    else:
        return render(request, 'todo/login.html')


def register_redirect(request):
    return render(request, 'todo/register.html')


def login_redirect(request):
    return render(request, 'todo/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

