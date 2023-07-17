from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from app1.models import Student, Branch, Book, AsBook


# Create your views here.
def home(request):
    return render(request,'home.html')


def admin_signup(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=name).exists():
            d = {'nameif':True}
            return render(request,'admin_signup.html', d)
        elif User.objects.filter(email=email).exists():
            d = {'emailif': True}
            return render(request, 'admin_signup.html', d)
        else:
            user = User.objects.create_superuser(username=name,email=email,password=password)
            user.save()
            return redirect('login')
    return render(request,'admin_signup.html')



def student_signup(request):
    b = Branch.objects.all()
    if request.method == 'POST':
        s = Student()
        s.name = request.POST['name']
        s.password = request.POST['password']
        s.phno = int(request.POST['phno'])
        s.branch = Branch.objects.get(branch=request.POST['branch'])
        s.semester = int(request.POST['semester'])
        if Student.objects.filter(name=s.name).exists():
            return render(request,'student_signup.html',{'data':b,'nameif': True})
        else:
            s.save()
            return render(request,'login.html')
    return render(request,'student_signup.html',{'data':b})


def login(request):
    if request.method=="POST":
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name,password=password)
        if user is not None:
            if user.is_superuser:
                return render(request,'adminhome.html',{'msg':False})
            else:
                return render(request, 'login.html', {'msg': True})
        elif Student.objects.filter(Q(name=name) & Q(password=password)).exists():
            request.session['name'] = name
            return render(request,'studenthome.html')
        else:
            return render(request, 'login.html', {'msg': True})
    else:
        return render(request,'login.html')


def add_book(request):
    b = Branch.objects.all()
    if request.method=="POST":
        book = Book()
        book.bookname = request.POST['book']
        book.authorname = request.POST['author']
        book.branch = Branch.objects.get(branch=request.POST['branch'])
        if Book.objects.get(bookname=book.bookname):
            d = {'bname':True,'data':b}

            return render(request,'add_book.html',d)
        else:
            book.save()
            save = {'save': True,'data':b}
            return render(request,'add_book.html',save)
    return render(request,'add_book.html',{'data':b})


def admin_display(request):
    b = Book.objects.all()
    return render(request,'admin_display.html',{'data':b})


def book_update(request,id):
    b = Book.objects.get(id=id)
    branch = Branch.objects.all()
    if request.method =="POST":
        b.bookname = request.POST['book']
        b.authorname = request.POST['author']
        b.branch = Branch.objects.get(branch=request.POST['branch'])
        b.save()
        return redirect('admin_display')

    return render(request,'displayupdate.html',{'data':b,'branch':branch})


def book_delete(request,id):
    b = Book.objects.get(id=id)
    b.delete()
    return redirect('admin_display')


def assign_book(request):
    b = Book.objects.all()
    a = AsBook()
    if request.method=="POST":
        a.student_name = request.POST['name']
        a.book_name = Book.objects.get(bookname=request.POST['book'])
        a.start_date = request.POST['sdate']
        a.end_date = request.POST['edate']
        if Student.objects.filter(name=a.student_name).exists():
            a.save()
            return render(request,'assignbook.html',{'data':True,'book':b})
        else:
            a = {'std':True,'book':b}
            return render(request,'assignbook.html',a)

    return render(request,'assignbook.html',{'book':b})

def assigned_display(request):
    ab = AsBook.objects.all()
    return render(request,'assigndisplay.html',{'data':ab})

def assigned_update(request,id):
    b = Book.objects.all()
    ab = AsBook.objects.get(id=id)
    if request.method=="POST":
        ab.student_name = request.POST['name']
        ab.book_name = Book.objects.get(bookname=request.POST['book'])
        ab.start_date = request.POST['sdate']
        ab.end_date = request.POST['edate']
        ab.save()
        return render(request,'assigndisplay')

    return render(request,'assignedupdate.html',{'book':b,'user':ab})

def assigned_delete(request,id):
    ab = AsBook.objects.get(id=id)
    ab.delete()
    return redirect('assigned_display')


def logout(request):
    return render(request,'home.html')


def studenthome(request):
    return render(request,'studenthome.html')


def studentprofile(request):
    s = Student.objects.get(name=request.session['name'])
    return render(request,'studentprofile.html',{'std':s})


def studentdisplay(request):
    ab = AsBook.objects.filter(student_name=request.session['name'])


    return render(request,'studentdisplay.html',{'data':ab})


def studentupdate(request,id):
    s = Student.objects.get(id=id)
    b = Branch.objects.all()
    if request.method == 'POST':
        s.name = request.POST['upname']
        s.branch = Branch.objects.get(branch=request.POST['upbranch'])
        s.password = request.POST['uppassword']
        s.semester = int(request.POST['upsemester'])
        s.phno = int(request.POST['upphno'])
        s.save()
        return redirect('studentprofile')
    return render(request,'studentupdate.html',{'std':s,'data':b})