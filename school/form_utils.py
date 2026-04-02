from django import forms


class StyledFormMixin:
    """Ajoute des classes Bootstrap simples pour avoir un rendu propre."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            widget = field.widget
            existing = widget.attrs.get('class', '')

            if isinstance(widget, (forms.CheckboxInput,)):
                css = 'form-check-input'
            elif isinstance(widget, (forms.Select, forms.SelectMultiple)):
                css = 'form-select'
            elif isinstance(widget, (forms.FileInput,)):
                css = 'form-control'
            else:
                css = 'form-control'

            widget.attrs['class'] = f'{existing} {css}'.strip()
            widget.attrs.setdefault('placeholder', field.label or name.replace('_', ' ').title())

        for field_name in ('password1', 'password2', 'password'):
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.pop('placeholder', None)
