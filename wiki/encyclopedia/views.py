from urllib import request
import markdown
import random

from django.shortcuts import redirect, render
from . import util



def index(request):
        if request.method == "POST":
            name_page = str(request.POST.get('q'))
            list_of_entries = util.get_entry(name_page)
            
            if(list_of_entries):
                return redirect("page", name=name_page)
            else:
                return redirect("search", name=name_page)
    
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries() 
        })

def entr(request, name):
    
    if request.method == "POST":
            name_page = str(request.POST.get('q'))
            list_of_entries = util.get_entry(name_page)
            
            if(list_of_entries):
                return redirect("page", name=name_page)
            else:
                return redirect("search", name=name_page)
                
    wiki = util.get_entry(name)
    return render(request, "encyclopedia/page.html", {
        "page": wiki,   
        "name": name
    })
    
def create(request):
    
    if request.method == "POST":
        
        name_page = str(request.POST.get('q'))
        list_of_entries = util.get_entry(name_page)
        if(list_of_entries):
            return redirect("page", name=name_page)
        elif(name_page == None):
            print("")
        elif(name_page != "None"):
            return redirect("search", name=name_page)
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        list = util.list_entries()
        
        if(content == "" or title == ""):
             return render(request, "encyclopedia/error.html", {
                "error": "Content or title of this page is empty"
            })
        elif(title not in list):
            util.save_entry(title, content)
            return redirect("page", name=title)
        
        else:
            return render(request, "encyclopedia/error.html", {
                "error": "This page's already exist"
            })
        
    
    return render(request, "encyclopedia/create.html")



def edit(request, name):
    content = util.get_entry(name)
    
    if request.method == "GET":
        
        return render(request, "encyclopedia/edit.html", {
            "name": name,
            "content": content
        })
    if request.method == "POST":
        
        name_page = str(request.POST.get('q'))
        list_of_entries = util.get_entry(name_page)
        if(list_of_entries):
            return redirect("page", name=name_page)
        elif(name_page == None):
            print("")
        elif(name_page != "None"):
            return redirect("search", name=name_page)
        
        
        title = request.POST.get('title')
        cont = request.POST.get('content')
        
        util.save_entry(title, cont)
        
        return redirect("page", name=title)
    
    
def search(request, name):
    
    if request.method == "GET":
        
        entries = util.list_entries()
        
        entries = util.rel_entry(name)
        
        return render(request, "encyclopedia/search.html", {
            "name": name,
            "entries": entries,
        })
       
    if request.method == "POST":
        name_page = str(request.POST.get('q'))
        list_of_entries = util.get_entry(name_page)
        
        if(list_of_entries):
            return redirect("page", name=name_page)
        else:
            return redirect("search", name=name_page)
    





def rand(request):
    
    list = util.list_entries()
    
    name = random.choice(list)
    return redirect("page", name=name)
    
    