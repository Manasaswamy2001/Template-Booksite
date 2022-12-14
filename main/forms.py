from django import forms
from .models import *


# book add form
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','author','published_year','image')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('comment', 'rating')
