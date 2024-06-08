from django import forms    # formulários Django
from .models import Artigo, Review, Autor


class ArtigoForm(forms.ModelForm):
  class Meta:
    model = Artigo      # classe para a qual é o formulário
    fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'