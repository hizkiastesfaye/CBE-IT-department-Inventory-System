from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
# Create your views here.
from .models import Items
from staff.models import Request


# new_username='abebe'
class dashboardView(View):
    store_ids = 0
    def get(self,request):
        ano_user=request.session.get('usernamee','')
        it = Items.objects.all()
        try:
            item_get=int(request.GET.get('store_id',''))
            print(type(item_get))
            edit_it = Items.objects.get(id=item_get)
            dashboardView.store_ids = item_get
            return render(request,"store/dashboard.html",{
            'username':ano_user,
            'itms':it,
            'edit_it':edit_it
        })
        except:

            try:
                delete_get=int(request.GET.get('delete_id',''))
                deleteItem= Items.objects.get(id=delete_get)
                deleteItem.delete()
                return render(request,"store/dashboard.html",{
                    'username':ano_user,
                    'itms':it
                })
            except:
                print('okay')
                return render(request,"store/dashboard.html",{
                    'username':ano_user,
                    'itms':it
                })
        


    def post(self,request):
       
        itemms = request.POST
        lower_item = itemms['item_type'].lower()
        if Items.objects.filter(id=dashboardView.store_ids).exists():
            one_item = Items.objects.get(id=dashboardView.store_ids)
            one_item.item=lower_item
            one_item.quantity= itemms['quantity']
            one_item.save()
        else:
            if itemms is not None:
                
                if Items.objects.filter(item=lower_item).exists():
                    sum=0
                    one_item=Items.objects.get(item=lower_item)
                    sum = int(itemms['quantity']) + one_item.quantity
                    one_item.quantity=sum
                else:
                    one_item=Items(item=lower_item, quantity=int(itemms['quantity']))  
                one_item.save()
        dashboardView.store_ids=0
        return redirect("dashboard_store")

# class helloview(View):
#     def get(self,request):
#         return(HttpResponse('hello people! hasfex'))
    
# class Itemsview(View):
#     def get(self,request):
#         lis = [0,1,2,3]
#         it = Items.objects.all()
#         return render(request,"store/items.html",{
#             'itms':it,
#             'lis':lis
#         })
#     def post(self,request):
#         pass
# def Items(request):
   

class Checkoutview(View):
    def get(self,request):
        try:
            print("-----------not yet----------------------")
            requ_check = int(request.GET.get('approve_id',''))
            print("--------------------------------------------------------")
            print(requ_check)
            requ_is = Request.objects.get(id=requ_check)
            item_quantity=Items.objects.get(item=requ_is.item)
            difference = item_quantity.quantity - requ_is.quantity
            item_quantity.quantity=difference
            item_quantity.save()
            requ_is.is_approved=True
            
            requ_is.save()
        except:
            print('okay what is prob')
        print('++++++++++++++++++++++++++===================')
        requ = Request.objects.filter(is_approved=False)
        requ_True = Request.objects.filter(is_approved=True)

        return render(request,"store/checkout.html",{

            'requ':requ,
            'requ_True':requ_True,
            'username':request.session.get('usernamee',''),
        })

# class Add_itemview(View):
#     def get(self,request):
#         return render(request,"store/add_item.html",)
#     def post(self,request):
       
#         itemms = request.POST
       
#         print(itemms)
#         if itemms['item_type'] is not None and itemms['quantity'] is not None:
#             one_item=Items(item=itemms['item_type'], quantity=itemms['quantity'])
#             # one_item.save()
#             return redirect("dashboard")


