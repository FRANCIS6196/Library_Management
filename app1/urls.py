from django.urls import path

from app1 import views

urlpatterns = [
    #MAIN PAGE URLS
    path('',views.home,name='home'),
    path('admin_signup',views.admin_signup,name='admin_signup'),
    path('student_signup',views.student_signup,name='student_signup'),
    path('login',views.login,name='login'),

    #ADMIN URLS
    path('admin_add',views.add_book,name='admin_add'),
    path('admin_display',views.admin_display,name='admin_display'),
    path('book_update/<int:id>',views.book_update,name='book_update'),
    path('book_delete/<int:id>',views.book_delete,name='book_delete'),
    path('assign_book',views.assign_book,name='assign_book'),
    path('assigned_display',views.assigned_display,name='assigned_display'),
    path('assigned_update/<int:id>',views.assigned_update,name='assigned_update'),
    path('assigned_delete/<int:id>',views.assigned_delete,name='assigned_delete'),
    path('logout',views.logout,name='logout'),

    # STUDENT URLS
    path('studenthome',views.studenthome,name='studenthome'),
    path('studentprofile',views.studentprofile,name='studentprofile'),
    path('studentdisplay',views.studentdisplay,name='studentdisplay'),
    path('studentupdate/<int:id>',views.studentupdate,name='studentupdate'),

]