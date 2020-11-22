from django import template

register = template.Library()


@register.simple_tag()
def get_lang_title(lang, langMn, langEn, langFr):
    if lang == "mn":
        return langEn.get("name_local").title()
    else:
        return langMn.get("name_local").title()
