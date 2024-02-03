from django.shortcuts import render,HttpResponse,redirect
from bookapp.models import Book
# Create your views here.
def homepage(request):
    data=Book.objects.all()
    context={}
    context['books'] = data 
    return render(request,'homepage.html',context)

def addbook(request):    
    if request.method=="GET":
        print("inside get change to post")
        return render(request,'addbook.html')
    else:
        print("within post ")
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        b=Book.objects.create(title=title,price=price,author=author)
        b.save()
        print("added book ",title,author,price)
        return render(request,'addbook.html')


def delete(request,bookid):
    b=Book.objects.filter(id=bookid)
    b.delete()
    return redirect('/homepage')

def update(request,bookid):
    if request.method=="GET":
        b= Book.objects.filter(id=bookid)
        print(b[0])
        context={}
        context['book'] = b[0]
        return render(request,'updatebook.html',context)
    else:
        print("within post ")
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        b=Book.objects.filter(id=bookid)
        b.update(title=title,price=price,author=author)
        print("added book ",title,author,price)
        return redirect('/homepage')

