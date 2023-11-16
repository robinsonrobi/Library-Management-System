
from email.policy import default
from enum import unique
from mongoengine import Document, fields


class Student(Document):
    username=fields.StringField(max_length= 255)    
    Registration_No=fields.IntField()
    email=fields.StringField()
    Password=fields.StringField()

    def to_json(self):
        return{
            "username" : self.username,
            "rno" : self.Registration_No,
            "email" : self.email,
            "password" : self.Password,
        }
class librarian(Document):
    username=fields.StringField()
    rno=fields.IntField()
    email=fields.StringField()
    password=fields.StringField()

    def to_json(self):
        return{
            "username" : self.username,
            "rno" : self.rno,
            "email" : self.email,
            "password" : self.password,            
        }
class Books(Document):
    bookname=fields.StringField()
    bookid=fields.StringField()
    author=fields.StringField()
    summary=fields.StringField()
    nobooks=fields.IntField()
    def to_json(self):
        return{
            "bookname" : self.bookname,
            "bookid" : self.bookid,
            "author" : self.author,
            "summary" : self.summary,
            "nobooks" : self.nobooks,                        
        }
class Ordbooks(Document):
    bookname=fields.StringField()
    bookid=fields.StringField()
    studentrno=fields.StringField()
    def to_json(self):
        return{
            "bookname" : self.bookname,
            "bookid" : self.bookid,
            "rno":self.studentrno,   
        }
class Status(Document):
    studentrno=fields.StringField()
    bookname=fields.StringField()
    bookid=fields.IntField()
    status=fields.IntField(default=0)
    pending=fields.IntField(default=0)
    returnb=fields.IntField(default=0)

    def to_json(self):
        return{
            "rno":self.studentrno,
            "bookname" : self.bookname,
            "bookid" : self.bookid,
            "status":self.status,
            "pending":self.pending,
            "returnb":self.returnb,
    }
