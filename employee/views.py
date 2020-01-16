from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html')

def GenerateFunc(request):   
    fname = request.POST['empname']
    month = request.POST['month']
    year = request.POST['year']
    amount = request.POST['amount']
    data = [fname,month,year,amount]
    f = open('file.txt','w')
    f.write(data[0])
    return render(request,'result.html')