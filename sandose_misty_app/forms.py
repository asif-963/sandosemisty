from django import forms
from .models import ContactModel, NearByPlace, ClientReview, Gallery, Folder, Booking, RoomPrice



# Contact us
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'

# NearByPlaceForm
class NearByPlaceForm(forms.ModelForm):
    class Meta:
        model = NearByPlace
        fields = '__all__'

# Clien Review
class ClientReviewForm(forms.ModelForm):
    class Meta:
        model = ClientReview
        fields = '__all__'

# Gallery
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'

# Folder
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = '__all__'


# Booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'  # You can choose specific fields if you don't need all fields
        
       



