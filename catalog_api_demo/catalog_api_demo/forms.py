from django import forms


class CourseForm(forms.Form):
	term       = forms.CharField(label='term', required=True)
	subject    = forms.CharField(label='subject', required=False)
	course_num = forms.CharField(label='course_num', required=False)
	q          = forms.CharField(label='q', required=False)
	page_size  = forms.CharField(label='page_size', required=False)
	page_num   = forms.CharField(label='page_num', required=False)
