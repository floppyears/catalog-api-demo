from django import forms

term_choices = (('fall', 'Fall'), ('winter', 'Winter'), ('spring', 'Spring'), ('summer', 'Summer'))


class CourseForm(forms.Form):
	year       = forms.CharField(label='Year', required=True)
	term       = forms.ChoiceField(label='Term', widget=forms.RadioSelect, choices=term_choices, required=True)
	subject    = forms.CharField(label='Subject', required=True)
	course_num = forms.CharField(label='Course Number', required=False)
	q          = forms.CharField(label='Query', required=False)
	page_size  = forms.CharField(label='Page Size', required=False, widget=forms.TextInput(attrs={'placeholder': '10 (Default)'}))
	page_num   = forms.CharField(label='Page Number', required=False, widget=forms.TextInput(attrs={'placeholder': '1 (Default)'}))


class TermForm(forms.Form):
	is_all    = forms.BooleanField(label='All', required=False)
	is_open   = forms.BooleanField(label='Open', required=False)
	year      = forms.CharField(label='Year', required=True)
	term      = forms.ChoiceField(label='Term', widget=forms.RadioSelect, choices=term_choices, required=True)
	page_size = forms.CharField(label='Page Size', required=False, widget=forms.TextInput(attrs={'placeholder': '10 (Default)'}))
	page_num  = forms.CharField(label='Page Number', required=False, widget=forms.TextInput(attrs={'placeholder': '1 (Default)'}))


class PageForm(forms.Form):
	page_link = forms.CharField(label='Page Link', required=True)
