from django import forms

from .models import booking

class dateinput(forms.DateInput):
    input_type = 'date'

class bookingform(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        widgets = {
          'booking_date' : dateinput(),
        }

        labels ={
            'p_name':"Patient Name: ",
            'p_phone':"Patient phone:",
            'p_email':"Patient email:",
            'doc_name':"Doctor Name:",
            'booking_date':"Patient Name:",
        

        }