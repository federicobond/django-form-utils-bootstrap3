from __future__ import unicode_literals

from django import forms
from django.template import Template, Context
from form_utils.forms import BetterForm
from form_utils_bootstrap3.renderers import BetterFormRenderer


class TestForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()


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


class TestBetterFormFull(BetterForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        fieldsets = [
            ('basic', {
                'fields': ['first_name', 'last_name'],
                'legend': 'Basic Information',
                'classes': ['custom-class'],
                'description': 'This is the description.'
            })
        ]


def test_renderer_outputs_fielsets():
    form = TestBetterForm()
    rendered = BetterFormRenderer(form).render()
    assert '<fieldset>\n<legend>Basic Information</legend>\n' in rendered
    assert '<div class="form-group">' in rendered
    assert '</fieldset>' in rendered


def test_renderer_handles_classes():
    form = TestBetterFormFull()
    rendered = BetterFormRenderer(form).render()
    assert '<fieldset class="custom-class">' in rendered


def test_renderer_handles_description():
    form = TestBetterFormFull()
    rendered = BetterFormRenderer(form).render()
    assert '</legend>\n<p>This is the description.</p>' in rendered


def test_rendered_works_on_default_forms():
    form = TestForm()
    rendered = BetterFormRenderer(form).render()
    assert '<div class="form-group">' in rendered


def test_renderer_configuration():
    template = Template('{% load bootstrap3 %}{% bootstrap_form form %}')
    context = Context({'form': TestBetterForm()})
    rendered = template.render(context)
    assert '<fieldset>' in rendered
