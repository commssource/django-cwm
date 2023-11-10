from django.shortcuts import render
from django.db.models import Q, F
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product, OrderItem
from store.models import Order



def say_hello(request):
    # try:
    #     product = Product.objects.get(pk=1)
    # except ObjectDoesNotExist:
    # call the first method of the QuerySet
    # product = Product.objects.filter(pk=1).first()
    # call if the product is exists in the QuerySet it return True or False

    # find product by range
    # query_set = Product.objects.filter(unit_price__range=(20, 30)) 
    
    # find product contains in the QuerySet
    # query_set = Product.objects.filter(title__icontains='dec')    
    # find product filter by date in the QuerySet
    # query_set = Order.objects.filter(last_update__year=2020) 
    #fine customer by id in the QuerySet
    #query_set = Order.objects.filter(customer__id=3)  
    # fine multiple product in the QuerySet
        # option 1
    #query_set = Product.objects.filter(inventory__lt= 10, unit_price__gt=10) 
        # option 2 using chain the filter method by apply the 2nd filter on the 1st filter
    #query_set = Product.objects.filter(inventory__lt= 10).filter(unit_price__gt=10)
    
    # filer using OR operator using Q object ~Q is NOT operator
    # query_set = Product.objects.filter(Q(inventory__lt= 10) | Q(unit_price__gt=20))
    
    # filer using using F object to reference fields "if price=10 etc" ~F is NOT operator
    #query_set = Product.objects.filter(inventory=F('unit_price'))
    
    # fine multiple product in the QuerySet
    #query_set = Order.objects.filter(customer__id=3)    
    
    # sort product in the QuerySet
    #query_set = Product.objects.order_by('-title') 
    
    # sort product in the QuerySet by multiple fields
    #query_set = Product.objects.order_by('-unit_price','-title') # -title is desc order
    # sort product in the QuerySet by unit_price and select 1st item in the list
        # option 1 order_by return QuerySet
    #product = Product.objects.order_by('unit_price')[0] # -title is desc order
    
    # sort product in the QuerySet by unit_price and select 1st item in the list
        # option 2 using earliest latest method these methods return the object not the QuerySet
    # product = Product.objects.earliest('unit_price') # -title is desc order
    
    # Limit the QuerySet result
    # this method will return the QuerySet of 1st 5 items in the list but 5 on the 1st page using pagination (python array slicing)
    #query_set = Product.objects.all()[1:5]
    
    # Selecting fields to query from database of selected fields only using values method. Values method return bunch of dictionaries in the QuerySet not product objects
    query_set = Product.objects.values('id','title', 'unit_price', 'collection__title')
    
    # Selecting fields to query from database of selected fields only using values_list method. Values method return bunch of tupples in the QuerySet not product objects
    # query_set = Product.objects.values_list('id','title', 'unit_price', 'collection__title')
    
    # Select product that has been ordered and sort them by the order title
    query_set = Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct()).order_by('title') # distinct method remove the duplicate items in the QuerySet
    
    return render(request, 'hello.html', {'name': 'Akbar', 'products': list(query_set)})
    # if not returnig the query_set but returing the 1st item in the list
    #return render(request, 'hello.html', {'name': 'Akbar', 'product':product} )
