from django import forms

from .models import Tag, Task


class DateInput(forms.DateInput):
    input_type = "date"


class TaskForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Content*",
                                      "style": "padding: 10px"}),
        label=""
    )
    is_completed = forms.BooleanField()
    deadline = forms.DateTimeField(
        widget=DateInput(attrs={"style": "padding: 10px"})
    )
    tags = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Name*",
                                      "style": "padding: 10px"}),
        label=""
    )

    class Meta:
        model = Tag
        fields = "__all__"
