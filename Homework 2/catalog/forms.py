from django.core.exceptions import ValidationError
from django.forms import ModelForm
from catalog.models import Product

forbidden_words = ["казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at',)

    def clean_name(self):
        name = self.cleaned_data['name']
        words_in_name = name.split()
        for word in words_in_name:
            if word.lower() in forbidden_words:
                raise ValidationError("Название не должно содержать запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        for word in forbidden_words:
            if word.lower() in description:
                raise ValidationError("Описание не должно содержать запрещенные слова")
        return description
