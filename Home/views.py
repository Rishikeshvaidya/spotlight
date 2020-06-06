from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from .models import Registers
from .models import notification
from .models import gdt
from .models import pptt
from .models import judge
from .models import win
from .forms import notificationform
#Create your views here.
#def homepage(request):

#    p = notification.objects.all()
#    w=win.objects.all()
#    return render(request, "Home/index.html", {'list': p,'w':w})

def homepage(request):
    p = notification.objects.all()
    w=win.objects.all()
    return render(request, "Home/hom.html", {'list': p,'w':w})

def loginpage(request):
    return render(request,"Home/login.html")


def Register(request):
    return render(request, "Home/Register.html")


def Registersubmit(request):

    srname = request.POST["srname"]
    sbranch= request.POST["sbranch"]
    syear= request.POST["syear"]
    mno = request.POST["mno"]
    srno= request.POST["srno"]
    spass= request.POST["spass"]
    email= request.POST["email"]
    reg=Registers(stname=srname,branch=sbranch,year=syear,mn=mno,rno=srno,remail=email,passs=spass)

    reg.save()
    return render(request, "Home/login.html")


def loginformsubmit(request):


    rlist = Registers.objects.all()
    userr=0
    if request.method == "POST":
        nme=request.POST.get("user",False)
        passl=request.POST.get("passf",False)
        if nme == "root" and passl == "root":
            return render(request, "Home/adminpanel.html")
        if passl == "spotlight":
            p = pptt.objects.all()
            return render(request, "Home/judges.html", {'p': p})
        for i in rlist:
            if (nme==i.stname and passl==i.passs):
                userr =1
                id = i.id
                break
            else:
                userr=0


        if(userr==1):
            rg= Registers.objects.get(id=id)
            return render(request,"Home/success.html",{'rg':rg})
        else:
            print("incorrect credintials")
            return render(request, "Home/login.html")
    else:
        print("incredintial not entered")
        return render(request, "Home/index.html")


def noti(request):
    if request.method =="POST":
        form=notificationform(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
    else:

        form=notificationform()
    return render(request,"Home/adminpanel.html",{'form':form})

def show(request):
    x=notification.objects.all()
    return render(request, "Home/show.html", {'x': x})
def edit(request,id):
    noti=notification.objects.get(id=id)
    return render(request, "Home/edit.html", {'noti': noti})

def update(request,id):
    ins=notification.objects.get(id=id)
    form=notificationform(request.POST,instance=ins)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "Home/edit.html", {'ins': ins})

def delete(request,id):
    noti = notification.objects.get(id=id)
    noti.delete()
    return redirect('/show')

def editdelete(request):
    x = notification.objects.all()
    return render(request, "Home/show.html", {'x': x})

def gd(request,id):
    rg = Registers.objects.get(id=id)
    return render(request, "Home/gd.html", {'rg': rg})

def gdsubmit(request,id):
    rg = Registers.objects.get(id=id)
    date = request.POST.get("date")
    time = request.POST.get("time")
    p= gdt(stname=rg.stname, branch=rg.branch, year=rg.year, mn=rg.mn, rno=rg.rno,gemail=rg.remail,passs=rg.passs,cpass=rg.cpass,gdate =date,gtime=time)
    p.save()
    return render(request,"Home/login.html")
def ppt(request,id):
    rg = Registers.objects.get(id=id)
    return render(request, "Home/ppt.html", {'rg': rg})
def pptsubmit(request,id):
    l= Registers.objects.get(id=id)
    date = request.POST.get("date")
    time = request.POST.get("time")
    ppt = request.POST.get("ppt")
    q = pptt(stname=l.stname, branch=l.branch, year=l.year, mn=l.mn, rno=l.rno,pdate=date,ptime=time,ppttopic=ppt,pemail=l.remail ,passs=l.passs, cpass=l.cpass)
    q.save()
    return render(request, "Home/login.html")


def registerstudentinfo(request):
    p=Registers.objects.all()
    return render(request,"Home/registrestudinfo.html",{'p':p})

def gdstudentinfo(request):
    p=gdt.objects.all()
    return render(request,"Home/gdstudentinfo.html",{'p':p})


def pptstudentinfo(request):
    p=pptt.objects.all()
    return render(request,"Home/pptstudentinfo.html",{'p':p})

def judgesubmit(request):
    srname = request.POST["srname"]
    sbranch = request.POST["sbranch"]
    syear = request.POST["syear"]
    cc = request.POST["cc"]
    ef = request.POST["ef"]
    c= request.POST["c"]
    rot = request.POST["rot"]
    total=int(cc)+int(ef)+int(c)+int(rot)
    j = judge(stname=srname, branch=sbranch, year=syear, cc=cc,ef=ef,co=c,rt=rot,total=total)

    j.save()
    p = pptt.objects.all()
    return render(request, "Home/judges.html", {'p': p})

def pptevaluation(request,id):
    r=Registers.objects.get(id=id)
    j=judge.objects.all()
    userr = 0
    for i in j:
        if (r.stname == i.stname and r.branch == i.branch and r.year==i.year):
            j = judge.objects.get(id=i.id)
            return render(request, "Home/pptevoluation.html", {'j': j})
        else:
            userr = 0
    if(userr==0):
        print("student not found")
        return render(request, "Home/noresult.html")



def winner(request):
    j = judge.objects.all().order_by('-total')[:3]
    return render(request, "Home/winner.html", {'j': j})
def winnersubmit(request):
    sname = request.POST["sname"]
    sbranch= request.POST["sbranch"]
    syear= request.POST["syear"]
    rank = request.POST["rank"]
    w = win(stname=sname,year=syear,branch=sbranch,rank=rank)
    w.save()
    return render(request, "Home/adminpanel.html")

def deletee(request):
    w=win.objects.all()
    return render(request, "Home/delete.html",{'w':w})
def deletewinner(request,id):
    n = win.objects.get(id=id)
    n.delete()
    w = win.objects.all()
    return render(request, "Home/delete.html", {'w': w})