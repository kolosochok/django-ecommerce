from django import forms
from blog.models import Comment

class CommentFrom(forms.ModelForm):
	comment = forms.CharField(widget=forms.Textarea(attrs={
		'placeholder': 'Write comment', 
		'class': "form-control", 
		'id': "textAreaExample", 
		'rows': "4", 
		'style': "background: #fff;"}))

	class Meta:
		model = Comment
		fields = ['comment']
