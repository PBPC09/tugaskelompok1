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
<<<<<<< HEAD
    )
=======
    )
>>>>>>> 6e20312ef3086855cb1a5dba4b0e11c5ccf2df13
