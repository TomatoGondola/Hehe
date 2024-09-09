from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator 

# Create your views here.

def index(request):
    # ! get all data from the listing database
    listings = Listing.objects.all().order_by('list_date')
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    # ! pass database records into listings context
    context = {'listings': paged_listings}
    #contexts = { 'name' : 'NEDM', 'community' : 'The dirtiest of dirties', }
    return render(request, "listings/listings.html", context,)

def listing(request, listing_id):   
    return render(request, "listings/listing.html", )

def search(request):
    return render(request, "listings/search.html")

