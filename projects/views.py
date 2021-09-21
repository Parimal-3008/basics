from django.shortcuts import render
from django.http import HttpResponse

pro = [
    {
           'id':1,
           'name':'rohan',
           
    },
    {
           'id':2,
           'name':'mohan',
    },
    {
        'id':3,
           'name':'rohit',
    }
]
def home(request,id):
    to= None
    for i in pro:
        if(i['id']== id):
            to=i
            print(to['name'])
            break
        
    return render(request,'a2.html',{'obj':to } )



def about(request):
    no=108
    str='sayonara'
    dict = { 'number': no, 'message': str,'product': pro}
    return render(request,'a1.html',dict)    

