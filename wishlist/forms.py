from django import forms

class AddToWishlistForm(forms.Form):
    PREFERENCE_CHOICES = [
        (1, 'Not Interested'),
        (2, 'Maybe Later'),
        (3, 'Interested'),
        (4, 'Really Want It'),
        (5, 'Must Have')
    ]
    
    preference = forms.ChoiceField(
        label='How much do you like this book?',
        choices=PREFERENCE_CHOICES,
        widget=forms.RadioSelect
    )