from django.shortcuts import render
from django.shortcuts import redirect
from .models import student
from .forms import Form


# Create your views here.
def index(request):
    return render(request, 'studentapp/index.html', {'title' : 'Home'})

def form(request):
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
        return redirect('records')
    else:
        form = Form()
    context = {
        'title': 'Form',
        'form': form
    }
    return render(request, 'studentapp/form.html', context)

def records(request):
    students = student.objects.all()
    context = {
        'title' : 'Records',
        'students' : students
    }
    return render(request, 'studentapp/records.html', context)
