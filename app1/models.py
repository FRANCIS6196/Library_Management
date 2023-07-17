from django.db import models

# Create your models here.

class Branch(models.Model):
    branch = models.CharField(max_length=50)
    def __str__(self):
        return self.branch
class Student(models.Model):
    name = models.CharField(max_length=50)
    phno = models.BigIntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    semester = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    bookname = models.CharField(max_length=50)
    authorname = models.CharField(max_length=50)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.bookname

class AsBook(models.Model):
    student_name = models.CharField(max_length=50)
    book_name = models.ForeignKey(Book,on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
