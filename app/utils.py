from django.forms.utils import ErrorList


class BootstrapError(ErrorList):
    def __str__(self):
        return self.as_divs()

    def as_divs(self) -> str:
        if not self: return ''
        return '<div>%s</div>' % ''.join(
            ['<div class="alert alert-danger">%s</div>' % e for e in self])