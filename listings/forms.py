from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'category', 'address', 'city', 'state', 'zipcode', 'description', 'price', 'photo_main', 'photo_1', 'photo_2', 'photo_3', 'photo_4', 'photo_5', 'photo_6']
    
class UpdateForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['title','description','price','photo_main']