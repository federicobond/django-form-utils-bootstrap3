from __future__ import unicode_literals

from bootstrap3.renderers import FormRenderer
from bootstrap3.forms import render_field


class BetterFormRenderer(FormRenderer):

    def render_fieldset(self, fieldset):
        output = []

        output.append('<fieldset>')
        output.append('<legend>{}</legend>'.format(fieldset.legend))

        for field in fieldset:
            output.append(render_field(
                field,
                layout=self.layout,
                form_group_class=self.form_group_class,
                field_class=self.field_class,
                label_class=self.label_class,
                show_label=self.show_label,
                show_help=self.show_help,
                exclude=self.exclude,
                set_required=self.set_required,
                set_disabled=self.set_disabled,
                size=self.size,
                horizontal_label_class=self.horizontal_label_class,
                horizontal_field_class=self.horizontal_field_class,
            ))

        output.append('</fieldset>')

        return '\n'.join(output)

    def render_fields(self):
        has_fieldsets = getattr(self.form, 'fieldsets', None)
        if not has_fieldsets:
            return super(BetterFormRenderer, self).render_fields()

        rendered_fieldsets = []
        for fieldset in self.form.fieldsets:
            rendered_fieldsets.append(self.render_fieldset(fieldset))
        return '\n'.join(rendered_fieldsets)
