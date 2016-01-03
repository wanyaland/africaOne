__author__ = 'wanyama'

from django.forms.widgets import SubWidget
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.forms.util import flatatt
from django.utils.html import conditional_escape, format_html
from django.utils.encoding import StrAndUnicode, force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

@python_2_unicode_compatible
class StarsChoiceInput(SubWidget):
    """
    An object used by ChoiceFieldRenderer that represents a single
    <input type='$input_type'>.
    """
    input_type = None  # Subclasses must define this

    def __init__(self, name, value, attrs, choice, index):
        self.name = name
        self.value = value
        self.attrs = attrs
        self.choice_value = force_text(choice[0])
        self.choice_label = force_text(choice[1])
        self.index = index

    def __str__(self):
        return self.render()

    def render(self, name=None, value=None, attrs=None, choices=()):
        name = name or self.name
        value = value or self.value
        attrs = attrs or self.attrs
        if 'id' in self.attrs:
            label_for = format_html(' for="{0}_{1}"', self.attrs['id'], self.index)
        else:
            label_for = ''
        return format_html('<label{0}>{1} </label>', label_for, self.tag())

    def is_checked(self):
        return self.value == self.choice_value

    def tag(self):
        if 'id' in self.attrs:
            self.attrs['id'] = '%s_%s' % (self.attrs['id'], self.index)
            final_attrs = dict(self.attrs, type='radio', name=self.name, value=self.choice_value)
        if self.is_checked():
            final_attrs['checked'] = 'checked'
        return mark_safe(u'<input%s />' % flatatt(final_attrs))

class StarsRadioChoiceInput(StarsChoiceInput):
    input_type = 'radio'
    def __init__(self, *args, **kwargs):
        super(StarsRadioChoiceInput, self).__init__(*args, **kwargs)
        self.value = force_text(self.value)

@python_2_unicode_compatible
class StarsChoiceFieldRenderer(object):
    """
    An object used by RadioSelect to enable customization of radio widgets.
    """

    choice_input_class = None

    def __init__(self, name, value, attrs, choices):
        self.name = name
        self.value = value
        self.attrs = attrs
        self.choices = choices

    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield self.choice_input_class(self.name, self.value, self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return self.choice_input_class(self.name, self.value, self.attrs.copy(), choice, idx)

    def __str__(self):
        return self.render()

    def render(self):
        """
        Outputs a <ul> for this set of choice fields.
        If an id was given to the field, it is applied to the <ul> (each
        item in the list will get an id of `$id_$i`).
        """
        return mark_safe(u'\n%s\n' % u'\n'.join([u'%s'
                   % force_unicode(w) for w in self]))


class StarsRadioFieldRenderer(StarsChoiceFieldRenderer):
    choice_input_class = StarsRadioChoiceInput