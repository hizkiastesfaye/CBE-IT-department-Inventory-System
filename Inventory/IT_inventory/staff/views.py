from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForms
from .models import User,Request,staffDescription
from django.views import View
from store.models import Items
# Create your views here.
# request.session.get('usernamee','')=''

def greet(request):
    return (HttpResponse("Hello guys"))

def dashboard(request):
    uus=request.session.get('usernamee','')
    return render(request,"staff/dashboard.html",{
        'username':uus
    })


class item(View):
    def get(self,request):
        lis = [0,1,2,3]
        it = Items.objects.all()
        uus=request.session.get('usernamee','')
        return render(request,"staff/items.html",{
            'itms':it,
            'lis':lis,
            'username':uus
        })
    def post(self,request):
        pass

class checkoutView(View):
    def get(self,request):
        ano_delet=0
        uus=request.session.get('usernamee','')
        try:
            ano_delet=request.GET.get('deletes','')
            print("----------------===================")
            print(ano_delet,'============---------=========')
            # ano_delet=int(delet)
            delete_request = Request.objects.get(id = ano_delet)
            delete_request.delete()
            requ=Request.objects.filter(username=request.session.get('usernamee','')).order_by('is_approved')
            userr=User.objects.get(username=request.session.get('usernamee',''))
            # iitem = Request.objects.get(username=request.session.get('usernamee',''),id=userr.id)
            return render(request,"staff/checkout.html",{
                'username':request.session.get('usernamee',''),
                'requ':requ,
            })
        except:
            ano_delet=0
            requ=Request.objects.filter(username=request.session.get('usernamee','')).order_by('is_approved')
            userr=User.objects.get(username=request.session.get('usernamee',''))
            # iitem = Request.objects.get(username=request.session.get('usernamee',''),id=userr.id)
            return render(request,"staff/checkout.html",{
                'username':request.session.get('usernamee',''),
                'requ':requ,
 
            })

class Orders(View):
    new_id=0
    
    def get(self,request):
        try:
            errorrr=request.session.get('errorrs','')
            itemm_type=request.session.get('itemm_type','')
            itemm_quantity=request.session.get('quantity','')
            itemm_reason=request.session.get('reason','')

            del request.session['itemm_type']
            del request.session['quantity']
            del request.session['reason']
            print(errorrr,itemm_reason)
            return render(request,"staff/request.html",{
                'username':request.session.get('usernamee',''),
                'error':errorrr,
                'reasonn_item':itemm_type,
                'reasonn_quantity':itemm_quantity,
                'reasonn_reason':itemm_reason,
                'numb':1

            })
        except:
            try:
                if 'item_type' in request.session: del request.session['itemm_type']
                if 'quantity' in request.session: del request.session['quantity']
                if 'reason' in request.session: del request.session['reason']
                idd = request.GET.get('reason', '')
                Orders.new_id=int(idd)
                reqqest=Request.objects.get(id=idd)
                return render(request,"staff/request.html",{
                    'username':request.session.get('usernamee',''),
                    'reasonn':reqqest,
                    'numb':2
                
                })
            except:
                return render(request,"staff/request.html",{
                'username':request.session.get('usernamee',''),
                })

    def post(self,request):
        usee = User.objects.get(username=request.session.get('usernamee',''))
        req = request.POST
        # qunn=Items.objects.get(item=req['items_type'])
        # print(qunn.quantity)
        error_quantity='*Decrease number of items'

        print(type(Orders.new_id))
        if Request.objects.filter(id=Orders.new_id).exists():
            req_data =Request.objects.get(id=Orders.new_id)
            if Items.objects.filter(item=req['items_type']).exists():
                if Items.objects.get(item=req['items_type']).quantity >= int(req['quantity']):
                    req_data.item=req['items_type']
                else:
                    request.session['itemm_type']=req['items_type']
                    request.session['quantity']=req['quantity']
                    request.session['reason']=req['reason']
                    request.session['errorrs']=error_quantity
                    return redirect ('requests_staff')
            else:
                request.session['itemm_type']=req['items_type']
                request.session['quantity']=req['quantity']
                request.session['reason']=req['reason']
                request.session['errorrs']='*no match to this item'
                return redirect ('requests_staff')
            req_data.quantity=req['quantity']
            req_data.reason=req['reason']
        else:
            if Items.objects.filter(item=req['items_type']).exists():
                
                if Items.objects.get(item=req['items_type']).quantity >= int(req['quantity']):
                    req_data=Request(username=request.session.get('usernamee',''),item=req['items_type'],quantity=req['quantity'],reason=req['reason'],userRequest=usee)
                else:
                    request.session['itemm_type']=req['items_type']
                    request.session['quantity']=req['quantity']
                    request.session['reason']=req['reason']
                    request.session['errorrs']=error_quantity
                    return redirect ('requests_staff')

            else:
                      
                request.session['itemm_type']=req['items_type']
                request.session['quantity']=req['quantity']
                request.session['reason']=req['reason']
                request.session['errorrs']='*no match to this item'
                return redirect ('requests_staff')
 
        # print("_+_+_+_+_+_+_+_+_+_+_+___+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_")
       
        req_data.save()
        Orders.new_id=0
        return redirect ("requests_staff")

class request_noView(View):
    def get(self,request):
            uus=request.session.get('usernamee','')
            descript=staffDescription.objects.filter(username=uus).order_by('-date')
            return render(request,"staff/requests_no.html",{
                'username':uus,
                'descript':descript,
                
    
            })
    def post(self,request):
        # print('-----------------------------+++++++++++++++++++++----------')
        des=request.POST
        uus=request.session.get('usernamee','')
        userss= User.objects.get(username=uus)
        descript=staffDescription.objects.filter(username=uus).order_by('-date')
        staffdescri = staffDescription(username=uus, description=des['description'], userRequest=userss)
        staffdescri.save()
        return render(request,"staff/requests_no.html",{
            'username':uus,
            'descript':descript,
        })

def signup(request):

    if request.method == 'GET':
        return render(request,"staff/signup.html",)
    else:
        usern = request.POST
        if usern['responsibility'] == 'select':
            error='*select your responsiblity!'
            return render(request,"staff/signup.html",{
                'error':error
            })
        if usern['password'] != usern['confirmPassword']:
            error='*check your confirm password!'
            return render(request,"staff/signup.html",{
                'error':error
            })
        
        usermodel = User(fullname=usern['fullName'],username=usern['username'],email=usern['email'],responsibility=usern['responsibility'],password=usern['password'])
        usermodel.save()
        print("the out put is --------------------------------------------")
        new_username=usern['username']
        request.session['usernamee'] = new_username
        if usern['responsibility'] == 'storeManager':
                return redirect('dashboard_store')
        else:
            return redirect('dashboard_staff')  # Redirect to the home page after successful login
    

def login(request):
    formss= LoginForms()
    if request.method == 'POST':
        uuuu = request.POST
        userlog=User.objects.filter(email=uuuu['email'])
        if userlog.exists() and userlog is not None and userlog[0].password == uuuu['password']:
            # global request.session.get('usernamee','')
            new_username=userlog[0].username
            request.session['usernamee'] = new_username
            if userlog[0].responsibility == 'storeManager':
                 return redirect('dashboard_store')
            else:
                return redirect('dashboard_staff',)  # Redirect to the home page after successful login
        else:
            error = '*wrong email or wrong password'
            return render(request,"staff/login.html",{
            'error': error,
            })

    else:
        return render(request,"staff/login.html",{
            'formm': formss,
        })
