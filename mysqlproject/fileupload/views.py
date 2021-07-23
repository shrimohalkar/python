from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import Book


# Create your views here.
def fileupload(request):

    data={}

    if request.method=='POST':
        upload_file=request.FILES['uploadfile']
        fs=FileSystemStorage()
        fname=fs.save(upload_file.name,upload_file)

        data['url']=fs.url(fname) # stores the file name

        print(upload_file.name)
        print(upload_file.size)

    return render(request,'fileupload.html',data)


def bookupload(request):
    if request.method == 'POST':
        b_title=request.POST.get('booktitle')
        b_uthor=request.POST.get('bookauthor')
        b_pdf = request.FILES['bookpdf']
        b_cover = request.FILES['bookcover']

        bookobj=Book() # Creating object

        bookobj.title=b_title
        bookobj.author=b_uthor
        bookobj.pdf=b_pdf
        bookobj.cover=b_cover
        bookobj.save()
        return redirect('/')

    return render(request,'upload_book.html')


def showbook(request):
    bookobj=Book.objects.all() #fetch the records
    return render(request,'showbook.html',{'book':bookobj})