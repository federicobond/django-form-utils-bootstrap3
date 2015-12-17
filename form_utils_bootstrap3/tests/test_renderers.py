from __future__ import unicode_literals

from django import forms
from form_utils.forms import BetterForm

from form_utils_bootstrap3.renderers import BetterFormRenderer

class TestBetterForm(BetterForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        fieldsets = [
            ('basic', {
                'fields': ['first_name', 'last_name'],
                'legend': 'Basic Information',
            })
        ]


def test_renderer_outputs_fielsets():
    form = TestBetterForm()
    rendered = BetterFormRenderer(form).render()
    assert '<fieldset>\n<legend>Basic Information</legend>\n' in rendered
    assert '<div class="form-group">' in rendered
    assert '</fieldset>' in rendered
