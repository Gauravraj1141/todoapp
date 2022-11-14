from django.shortcuts import render  , HttpResponse,redirect
from .models import todotask
from django.utils import timezone
# Create your views here.

def todos(request):
    context = {"success": False}
    if request.method == "POST" :
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title, desc)

        data = todotask(task_title = title , task_desc = desc)
        data.save()
        context = {"success": True}



    return render(request, "todo.html",context)


def tasks(request):
    todosdata = todotask.objects.all()
   
    data = {"alldata":todosdata}
    return render(request, "tasks.html",data)



def deleteTask(request, td):
    list = todotask.objects.filter(task_id = td)
    list.delete()

    return redirect("/tasks")

def updatetask(request,upid):
    if request.method == "POST":
        title = request.POST["title"]
        desc = request.POST["desc"]
        obj = todotask.objects.get(task_id = upid)
        obj.task_title = title
        obj.task_desc = desc
        obj.save()
        return redirect("/tasks")
        

    else:
        prevdata = todotask.objects.filter(task_id=upid)
        return render(request, "update.html",{"data":prevdata})

