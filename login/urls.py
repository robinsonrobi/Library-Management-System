from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('login/',views.login),
    path('login/valid/',views.sloginValid),
    path('login/books/',views.sloginValid),
    # path('login/sbooks/',views.sbooks),
    path('login/sbooks/mybooks/<rno>/',views.returnb),
    path('login/signup/',views.signup),
    path('login/signup/addrecord/',views.saddrecord),

    path('liblogin/',views.liblogin,name='librarianlogin'),
    path('liblogin/valid/',views.libValid),
    path('liblogin/bookspage/',views.books),
    path('liblogin/valid/signup/',views.signup),
    path('liblogin/libsignup/',views.libsignup),
    path('liblogin/libsignup/liblogin/signup/libaddrecord/',views.libaddrecords),
    path('liblogin/valid/goback/',views.libbooks),

    path('liblogin/valid/update/',views.update),
    path('liblogin/valid/update/updatebookdet/',views.updatebook),
    path('liblogin/valid/update/updated/',views.updatabookdet),
    

    # path('liblogin/valid/addbooks/',views.orderedbooks),
    path('liblogin/spage/<rno>/',views.registerAbooks),
    path('login/valid/orderedbooks/<rno>/',views.registerbooks),

    path('login/valid/registered/',views.registered),


    path('login/valid/addbooks/',views.addbookss),
    path('login/valid/add/',views.addbooks),

    path('<rno>/<bookid>/<A>/',views.Astatus),
    # path('<rno>/<bookname>/<bookid>/<R>/',views.Astatus),
    path('login/valid/status/<rno>/show/',views.student_status),

    path('login/sbooks/mybooks/<rno>/<bookid>/RT/',views.returnbook),

    path('1/',views.ind)


    


    


]
