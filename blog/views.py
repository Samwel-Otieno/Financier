from django.shortcuts import render, redirect
from django.http import FileResponse
from django.contrib.auth.decorators import login_required
from .forms import *
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter




# Create your views here.

@login_required(login_url="/accounts/login/")
# Create blog view
def create_blog(request):
    if request.method=='POST':
        create_blog_form=Create_blog(request.POST, request.FILES)
        if create_blog_form.is_valid:
            instance= create_blog_form.save(commit=False)
            instance.owner=request.user
            instance.save()
            return redirect('blog:blogs')
        else:
            return redirect('blog:create_blog')
    else:
        create_blog_form=Create_blog()
    return render(request,'blog/create_blog.html',{'create_blog_form':create_blog_form})

#Render blogs view
def blog(request):
    blogs=Create_blogs.objects.all().order_by('created')
    return render(request, 'blog/blogs.html', {'blogs':blogs})

#Comments section view 
def comments(request):
    if (request.method=='POST'):
        comment_form=Comment(request.POST)
        if comment_form.is_valid():
            comment_form.save()
    else:
        comment_form=Comment()
    return render(request, 'blog/comments.html', {'comment_form':comment_form})

# PDF generator view

def generatepdf(request):
    # Create a file-like buffer to receive PDF data.
    buff = io.BytesIO()
    # create a canvas 
    canv=canvas.Canvas(buff, pagesize=letter, bottomup=0)

    # create a text object to be rendered in the canvas
    textobj=canv.beginText()
    textobj.setTextOrigin(inch,inch)
    textobj.setFont("Helvetica", 14)
   
    #add the text lines to be printed 
    articles=Create_blogs.objects.all()
    lines=[]
    
    for blogarticle in articles:
        lines.append(blogarticle)
        # lines.append(article.title)
        # lines.append(article.article)
        # lines.append(article.image)
        # lines.append(article.owner)
        # lines.append(article.created)
        # print a break line
        for i in range(0,10):
            print("**--**--", end="")
    #render the lines into the canvas 

    for line in lines:
        textobj.textLine(line)

    canv.drawText(textobj)
    canv.showPage()
    canv.save()
    buff.seek(0)
    
  


    return FileResponse(buff, as_attachment=True, filename='Articles.pdf')