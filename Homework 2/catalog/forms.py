from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField
from catalog.models import Product, Version

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Product
        exclude = (
            "created_at",
            "updated_at",
            "owner"
        )

    def clean_name(self):
        name = self.cleaned_data["name"]
        words_in_name = name.split()
        for word in words_in_name:
            if word.lower() in forbidden_words:
                raise ValidationError("Название не должно содержать запрещенные слова")
        return name

    def clean_description(self):
        description = self.cleaned_data["description"]
        for word in forbidden_words:
            if word.lower() in description:
                raise ValidationError("Описание не должно содержать запрещенные слова")
        return description


class ProductModeratorForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Product
        fields = ('is_published', 'description', 'category')


class VersionForm(FormStyleMixin, ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def clean_is_active(self):
        is_active = self.cleaned_data["is_active"]
        active_version = Version.objects.filter(is_active=True)
        if len(active_version) > 0 and is_active:
            raise ValidationError(
                f"""Активной может быть только одна версия. Сейчас активна версия №{active_version[0].number}.
                Снимите флаг активности со всех версий и попробуйте снова."""
            )
        else:
            return is_active
