from django import forms
from .models import OfficeInspection, DailyInspection


RESULT_OPTION = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

class OfficeInspectionForm(forms.ModelForm):
    class Meta:
        model = OfficeInspection

        exclude = [
            'timestamp',
            'updated',
            'image'
        ]
        

    plug = forms.ChoiceField(
            choices=RESULT_OPTION,
            widget = forms.RadioSelect,
            )

    power = forms.ChoiceField(
            choices=RESULT_OPTION,
            widget = forms.RadioSelect,
            )
    # ModelChoiceField

    '''
    def clean_plug(self):
        return self.data.get('plug')
    '''

class DailyInspectionForm(forms.ModelForm):
    
    impact = forms.MultipleChoiceField(
            choices = lambda: (item for item in DailyInspection.daily_insepction_impact),
            widget = forms.SelectMultiple(),
            #widget=forms.CheckboxSelectMultiple(),
            initial = ['environment'],
            #initial= lambda: [item for item in DailyInspection.daily_insepction_impact if item],
            required=True
            )
    

    def __init__(self, *args, **kwargs):
        super(DailyInspectionForm, self).__init__(*args, **kwargs)

    def clear_image_after_clear(self):
        if self.data.get('image_after-clear'):
            return "on"
        return None

    def clear_image_before_clear(self):
        if self.data.get('image_before-clear'):
            return "on"
        return None

    class Meta:
        model = DailyInspection

        exclude = [
            'timestamp',
            'updated',
        ]
        


    # ModelChoiceField

    '''
    def clean_plug(self):
        return self.data.get('plug')
    '''

class InspectionFilterForm(forms.Form):
    q = forms.CharField(label='Search', required=False)
    '''
    category_id = forms.ModelMultipleChoiceField(
        label='Category',
        queryset=Category.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required=False)
    '''
    cateory = forms.MultipleChoiceField(
            label='Category',
            choices = DailyInspection.daily_insepction_category,
            #widget = forms.SelectMultiple(),
            widget=forms.CheckboxSelectMultiple(),
            initial = None,
            required=False
            )    
    correct_status = forms.ChoiceField(
            label='correct status',
            choices = DailyInspection.daily_insepction_correction_status,
            widget=forms.RadioSelect(),
            required=False
            )   
    owner = forms.CharField(required=False)