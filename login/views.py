from django.shortcuts import render
from .models import Student, librarian,Books,Status
from django.http import HttpResponse 
from django.template import loader

def ind(request):
    return render(request,"index1.html")
def login(request):
    template = loader.get_template('login1.html')
    return HttpResponse(template.render({},request))

def signup(request):
    template = loader.get_template('signup1.html')
    return HttpResponse(template.render({},request))

def libsignup(request):
    template = loader.get_template('libsignup.html')
    return HttpResponse(template.render({},request))

def home(request):
    template= loader.get_template('index.html') 
    return HttpResponse(template.render({},request))

def books(request):
    booklist=list()
    for book in Books.objects():
        booklist.append(book.to_json())
    return render(request,"books1.html",{"booklist":booklist})

def libbooks(request):
    booklist=list()
    for book in Books.objects():
        booklist.append(book.to_json())
    return render(request,"books1.html",{"booklist":booklist})

def liblogin(request):
    template= loader.get_template('liblogin1.html') 
    return HttpResponse(template.render({},request))

def addbookss(request):
    template= loader.get_template('addbooks1.html') 
    return HttpResponse(template.render({},request))

def update(request):
    template= loader.get_template('update.html') 
    return HttpResponse(template.render({},request))

def registerbooks(request,rno):
    booklist=list()
    for book in Books.objects():
        booklist.append(book.to_json())
    return render(request,"registerbooks1.html",{"booklist":booklist,"rno":rno})
    
def registered(request):
    booklist=list()
    for book in Status.objects():
        booklist.append(book.to_json())
    return render(request,"registered1.html",{"booklist":booklist})

def student_status(request,rno):
    booklist=list()
    for book in Status.objects():
        if book['studentrno']==rno:
            booklist.append(book.to_json())
            
    return render(request,"status1.html",{"booklist":booklist})

def returnb(request,rno):
    booklist=list()
    for book in Status.objects():
        if book['status']==1 and book['studentrno']==rno:
            booklist.append(book.to_json())    
    return render(request,"return1.html",{"booklist":booklist,"rno":rno})

def saddrecord(request):
    username = request.POST['username']
    rno = request.POST['rno']
    email = request.POST['email']
    password= request.POST['password']
    confirm_password = request.POST['rpassword']

    flag = False

    if password == confirm_password:
        studentObjects_list = list()
        for stdnt in Student.objects():
            studentObjects_list.append(stdnt.to_json())

        for stdnt in studentObjects_list:
            if stdnt['rno'] == int(rno):
                error_message = "Roll No Already Exist"
                flag = True
                break
            if stdnt['email'] == email:
                error_message = "Email Id '" + email + "' Already Exist"
                flag = True
                break
    else:
        error_message = "Password did not match"
        flag = True
    
    if flag:
        return render(request, "signup1.html", {"error_message" : error_message})

    studentDetails = Student(username = username, Registration_No = rno, email = email,Password = password)
    studentDetails.save() 
    return render(request, 'login1.html')


def sloginValid(request):
    username = request.POST['username']
    password = request.POST['password']
    sobjlist=list()


    for stu in Student.objects():
        sobjlist.append(stu.to_json())

    flag=False
    for stu in sobjlist:
        if stu['username']==username and stu['password']==password:
            rno=stu['rno']
            flag=True
            break
        else:
            error_message = "Incorrect Username and Password"
            flag = False
    if flag:                
        bookobjlist=list()
        for book in Books.objects():
            book = book.to_json()
            sbookid = book['bookid']
            reg=Status.objects.filter( status = 1, studentrno = str(rno),bookid = int(sbookid))
            print(len(reg))
            if len(reg) != 0:
                continue
            bookobjlist.append(book)
        if len(bookobjlist)==0:
            bookobjlist=None
        return render(request,"sbooks1.html",{"booklist" : bookobjlist,"rno":rno})
    else:
        return render(request,'login1.html',{"error_message":error_message})


def libaddrecords(request):
    username = request.POST['username']
    rno = request.POST['rno']
    email = request.POST['email']
    password= request.POST['password']
    confirm_password = request.POST['rpassword']

    flag = False

    if password == confirm_password:
        lib_list = list()
        for lib in librarian.objects():
            lib_list.append(lib.to_json())


        for lib in lib_list:
            if lib['rno'] == int(rno):
                error_message = "Roll No Already Exist"
                flag = True
                break
            if lib['email'] == email:
                error_message = "Email Id '" + email + "' Already Exist"
                flag = True
                break
    else:
        error_message = "Password did not match"
        flag = True
    
    if flag:
        return render(request, "signup1.html", {"error_message" : error_message})

    libDetails = librarian(username = username, rno = rno, email = email,password = password)
    libDetails.save() 
    return render(request, 'liblogin1.html')

def libValid(request):
    username = request.POST['username']
    password = request.POST['password']
    lib_list=list()

    for lib in librarian.objects():
        lib_list.append(lib.to_json())


    flag=False
    for lib in lib_list:
        if lib['username']==username and lib['password']==password:
            flag=True
            break
        else:
            error_message = "Incorrect Username and Password"
            flag = False
    if flag:
        booklist=list()
        for book in Books.objects():
            booklist.append(book.to_json())
        return render(request,"books1.html",{"booklist":booklist})
    else:
        return render(request,'liblogin1.html',{"error_message":error_message})
def addbooks(request):
    bookname = request.POST['bookname']
    bookid = request.POST['bookid']
    author = request.POST['author']
    summary = request.POST['summary']
    nobooks = request.POST['nobooks']
    booklist=list()
    for book in Books.objects():
        booklist.append(book.to_json())
    flag=False
    for book in Books.objects():
        if book['bookname']==bookname and book['author']==author and book['bookid']==bookid:
            flag=True
            n=book['nobooks']+int(nobooks)
            print(n)
            book['nobooks']=n
            book.save()
            break
    if flag==False:
        add=Books(bookname=bookname,bookid=bookid,author=author,summary=summary,nobooks=nobooks)
        add.save()
        booklist=list()
        for book in Books.objects():
            booklist.append(book.to_json())
        return render(request,"books1.html",{"booklist":booklist})
    else:
        booklist=list()
        for book in Books.objects():
            booklist.append(book.to_json())
        return render(request,"books1.html",{"booklist":booklist})


def updatebook(request):
    find = request.POST.get("search")
    flag=False
    findlist=list()
    for book in Books.objects():
        if book['bookid']==find:
            findlist.append(book.to_json())
            flag=True 
            break
    
    if flag==False:
        error_message="Invalid Book ID"
        return render(request,'update.html',{"error_message":error_message})
    return render(request,"update.html",{"find":findlist})

    
def updatabookdet(request):
    bookname= request.POST.get('bookname')
    author=request.POST.get('author')
    summary=request.POST.get('summary')
    nobooks=request.POST.get('nobooks')
    bookid=request.POST.get('bookid')
    for book in Books.objects():
        if book['bookid']==bookid:
            book['bookname']=bookname
            book['author']=author
            book['summary']=summary
            book['nobooks']=nobooks
            book.save()
    booklist=list()
    for book in Books.objects():
        booklist.append(book.to_json())
    return render(request,"books1.html",{"booklist":booklist})
    

def registerAbooks(request,rno):
    bookname = request.POST['bookname']
    bookid = request.POST['bookid']
    booklist=list()
    for book in Books.objects():
        booklist.append(book.to_json())
    flag=False
    check=False
    for book in booklist:
        if book['bookname']==bookname and book['bookid']==bookid:
            check=True
            break
    statuslist=list()
    for s in Status.objects():
        statuslist.append(s.to_json())
    for s in statuslist:
        if s['rno']==rno and s['bookid']==int(bookid):
            flag=True
            break
            
    if flag==False and check==True:
        add=Status(studentrno=rno,bookname=bookname,bookid=bookid,status=0,pending=0)
        add.save()
        booklist=list()
        error_message="Book Requested Succussfully"
        for book in Books.objects():
            if book['bookid']==(bookid):
                book['nobooks'] -= 1
                book.save()
        for book in Books.objects():
            booklist.append(book.to_json())
        return render(request,"sbooks1.html",{"booklist":booklist,"error_message":error_message})

    elif flag==True and check==True:
        booklist=list()
        for book in Books.objects():
            booklist.append(book.to_json())
        error_message="Already you are booked in this book"
        return render(request,"registerbooks1.html",{"booklist":booklist,"error_message":error_message})

    else:
        booklist=list()
        for book in Books.objects():  
            booklist.append(book.to_json())
        error_message="Enter a valid Book details"
        return render(request,"registerbooks1.html",{"booklist":booklist,"error_message":error_message})

def Astatus(request,rno,bookid,A):
    if A=='A':
        flag=False
        booklist=list()
        for book in Status.objects():
            booklist.append(book.to_json())
        for booklendings in Status.objects():
            if booklendings['bookid'] == int(bookid) and booklendings['studentrno'] == (rno):
                booklendings['status'] = 1
                booklendings['pending'] = 0
                booklendings['returnb'] = 0
                booklendings.save()
                flag=True
        if flag:
            error_message="Book Approved"
            booklist=list()
            for book in Status.objects():
                booklist.append(book.to_json())
            return render(request,"registered1.html",{"error_message":error_message,"booklist":booklist})
    elif A=='R':
        flag=False
        booklist=list()
        for book in Status.objects():
            booklist.append(book.to_json())
        for booklendings in Status.objects():
            if booklendings['bookid'] == int(bookid) and booklendings['studentrno'] == (rno):
                booklendings['status'] = 0
                booklendings['pending'] = 1
                booklendings['returnb'] = 0
                booklendings.save()
                flag=True
        if flag:
            for book in Books.objects():
                if book['bookid']==(bookid):
                    book['nobooks'] += 1
                    book.save()
            error_message="Book Rejected"
            booklists=list()
            for book in Status.objects():
                booklists.append(book.to_json())
            return render(request,"registered1.html",{"error_message":error_message,"booklist":booklists})
def returnbook(request,rno,bookid):
    booklist=list()
    for book in Status.objects():
        booklist.append(book.to_json())
    for booklendings in Status.objects():
        if booklendings['bookid'] == int(bookid) and booklendings['studentrno'] == (rno):
            booklendings['status'] = 0
            booklendings['pending'] = 0
            booklendings['returnb'] = 1
            booklendings.save()
            flag=True
    if flag:
        for book in Books.objects():
            if book['bookid']==bookid:
                book['nobooks'] += 1
                book.save()
            error_message="Book Rejected"
        error_message="Returned Succussfully"
        return render(request,"return1.html",{"error_message":error_message})

        

    