from django import forms
from .models import Produto, UserProfile, Matricula


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome", "imagem", "preco"]  # Campos do formulário


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_pic"]  # Apenas o campo de foto

class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ['nome', 'email', 'plano', 'observacoes']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'plano': forms.TextInput(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }