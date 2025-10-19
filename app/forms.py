from .models import Blog
from django.forms import ModelForm

class blogForm(ModelForm):
    class Meta:
        model = Blog
        # Only expose editable fields; created/updated are auto-managed
        fields = ['title', 'body']
